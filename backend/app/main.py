from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1 import api_router
from app.db.base import Base
from app.db.session import engine
from app.middleware.logging_middleware import logging_middleware
from app.utils.logger import get_logger
from app.crud.user import role_crud, permission_crud
from sqlalchemy.orm import Session

logger = get_logger(__name__)

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize default roles and permissions
def init_db():
    """Initialize database with default roles and permissions"""
    from app.db.session import SessionLocal
    db = SessionLocal()
    try:
        # Create default permissions
        permissions_data = [
            ("view_employees", "View employees", "employee"),
            ("create_employee", "Create employee", "employee"),
            ("edit_employee", "Edit employee", "employee"),
            ("delete_employee", "Delete employee", "employee"),
            ("view_reports", "View reports", "report"),
            ("manage_users", "Manage users", "user"),
            ("manage_roles", "Manage roles", "user"),
        ]
        
        for perm_name, perm_desc, perm_cat in permissions_data:
            if not permission_crud.get_permission_by_name(db, perm_name):
                permission_crud.create_permission(db, perm_name, perm_desc, perm_cat)
        
        # Create default roles
        roles_data = [
            ("admin", "Administrator with full access"),
            ("manager", "Manager with limited admin access"),
            ("employee", "Regular employee"),
            ("viewer", "Read-only access"),
        ]
        
        for role_name, role_desc in roles_data:
            if not role_crud.get_role_by_name(db, role_name):
                role_crud.create_role(db, role_name, role_desc)
        
        logger.info("Database initialized with default roles and permissions")
    finally:
        db.close()

# Initialize database
init_db()

# Initialize FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="Employee Management System API"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add logging middleware
app.middleware("http")(logging_middleware)

# Include API routes
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.on_event("startup")
async def startup_event():
    logger.info(f"Starting {settings.PROJECT_NAME} v{settings.PROJECT_VERSION}")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info(f"Shutting down {settings.PROJECT_NAME}")

@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Welcome to Employee Management System",
        "version": settings.PROJECT_VERSION,
        "docs": "/docs"
    }

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}
