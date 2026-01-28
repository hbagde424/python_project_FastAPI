from fastapi import APIRouter
from app.api.v1.endpoints import employees, stats

api_router = APIRouter()
api_router.include_router(employees.router, prefix="/employees", tags=["employees"])
api_router.include_router(stats.router, prefix="/stats", tags=["statistics"])
