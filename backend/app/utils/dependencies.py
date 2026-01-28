from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthCredentials
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import verify_token
from app.crud.user import user_crud
from app.utils.logger import get_logger

logger = get_logger(__name__)

security = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    """Get current authenticated user"""
    token = credentials.credentials
    
    token_data = verify_token(token)
    if not token_data:
        logger.warning("Invalid token")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user = user_crud.get_user_by_id(db, token_data.user_id)
    if not user:
        logger.warning(f"User not found: {token_data.user_id}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not user.is_active:
        logger.warning(f"Inactive user: {user.email}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive"
        )
    
    return user

async def get_current_admin(
    current_user = Depends(get_current_user)
):
    """Get current admin user"""
    if not current_user.has_role("admin"):
        logger.warning(f"Non-admin user attempted admin action: {current_user.email}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user

async def get_current_manager(
    current_user = Depends(get_current_user)
):
    """Get current manager user"""
    if not (current_user.has_role("manager") or current_user.has_role("admin")):
        logger.warning(f"Non-manager user attempted manager action: {current_user.email}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Manager access required"
        )
    return current_user

def require_permission(permission_name: str):
    """Require specific permission"""
    async def permission_checker(current_user = Depends(get_current_user)):
        if not current_user.has_permission(permission_name):
            logger.warning(f"User {current_user.email} lacks permission: {permission_name}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permission '{permission_name}' required"
            )
        return current_user
    return permission_checker

def require_role(role_name: str):
    """Require specific role"""
    async def role_checker(current_user = Depends(get_current_user)):
        if not current_user.has_role(role_name):
            logger.warning(f"User {current_user.email} lacks role: {role_name}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Role '{role_name}' required"
            )
        return current_user
    return role_checker
