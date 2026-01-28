from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.auth_service import AuthService, RoleService, PermissionService
from app.schemas.auth import (
    RegisterRequest, LoginRequest, LoginResponse, UserResponse,
    RefreshTokenRequest, TokenResponse, ChangePasswordRequest,
    CreateRoleRequest, CreatePermissionRequest, RoleResponse,
    PermissionResponse, AssignRoleRequest
)
from app.utils.dependencies import get_current_user, get_current_admin
from app.utils.logger import get_logger
from app.toast import toast

logger = get_logger(__name__)
router = APIRouter()

# Authentication endpoints
@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(
    user_data: RegisterRequest,
    db: Session = Depends(get_db)
):
    """Register a new user"""
    logger.info(f"Register endpoint called for: {user_data.email}")
    user = AuthService.register(db, user_data)
    return user

@router.post("/login", response_model=LoginResponse)
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    """Login user"""
    logger.info(f"Login endpoint called for: {login_data.email}")
    result = AuthService.login(db, login_data)
    return {
        "user": result["user"],
        "access_token": result["access_token"],
        "refresh_token": result["refresh_token"]
    }

@router.post("/refresh", response_model=TokenResponse)
def refresh_token(
    request: RefreshTokenRequest
):
    """Refresh access token"""
    logger.info("Refresh token endpoint called")
    result = AuthService.refresh_access_token(request.refresh_token)
    return result

@router.post("/change-password")
def change_password(
    request: ChangePasswordRequest,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Change user password"""
    logger.info(f"Change password endpoint called for: {current_user.email}")
    
    if request.new_password != request.confirm_password:
        raise ValueError("Passwords do not match")
    
    AuthService.change_password(db, current_user.id, request.old_password, request.new_password)
    return {"message": "Password changed successfully"}

@router.get("/me", response_model=UserResponse)
def get_current_user_info(
    current_user = Depends(get_current_user)
):
    """Get current user information"""
    logger.info(f"Get current user endpoint called for: {current_user.email}")
    return current_user

# Role endpoints
@router.post("/roles", response_model=RoleResponse, status_code=status.HTTP_201_CREATED)
def create_role(
    role_data: CreateRoleRequest,
    current_user = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """Create a new role (Admin only)"""
    logger.info(f"Create role endpoint called by: {current_user.email}")
    role = RoleService.create_role(db, role_data.name, role_data.description, role_data.permission_ids)
    return role

@router.get("/roles", response_model=list[RoleResponse])
def get_all_roles(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all roles"""
    logger.info(f"Get all roles endpoint called by: {current_user.email}")
    roles = RoleService.get_all_roles(db)
    return roles

@router.post("/users/{user_id}/roles", status_code=status.HTTP_200_OK)
def assign_role_to_user(
    user_id: int,
    request: AssignRoleRequest,
    current_user = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """Assign role to user (Admin only)"""
    logger.info(f"Assign role endpoint called by: {current_user.email}")
    RoleService.assign_role_to_user(db, user_id, request.role_id)
    return {"message": "Role assigned successfully"}

# Permission endpoints
@router.post("/permissions", response_model=PermissionResponse, status_code=status.HTTP_201_CREATED)
def create_permission(
    permission_data: CreatePermissionRequest,
    current_user = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """Create a new permission (Admin only)"""
    logger.info(f"Create permission endpoint called by: {current_user.email}")
    permission = PermissionService.create_permission(
        db, permission_data.name, permission_data.description, permission_data.category
    )
    return permission

@router.get("/permissions", response_model=list[PermissionResponse])
def get_all_permissions(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all permissions"""
    logger.info(f"Get all permissions endpoint called by: {current_user.email}")
    permissions = PermissionService.get_all_permissions(db)
    return permissions
