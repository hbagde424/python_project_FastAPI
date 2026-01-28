from sqlalchemy.orm import Session
from app.crud.user import user_crud, role_crud, permission_crud
from app.schemas.auth import RegisterRequest, LoginRequest
from app.core.security import (
    verify_password, get_password_hash, create_access_token,
    create_refresh_token, verify_token, ACCESS_TOKEN_EXPIRE_MINUTES
)
from app.utils.exceptions import (
    EmailAlreadyExists, InvalidCredentials, UserNotFound,
    PasswordMismatch
)
from app.utils.logger import get_logger
from datetime import timedelta

logger = get_logger(__name__)

class AuthService:
    @staticmethod
    def register(db: Session, user_data: RegisterRequest):
        """Register a new user"""
        logger.info(f"Registering user: {user_data.email}")
        
        # Check if passwords match
        if user_data.password != user_data.confirm_password:
            logger.warning(f"Password mismatch for registration: {user_data.email}")
            raise PasswordMismatch()
        
        # Check if email already exists
        existing_user = user_crud.get_user_by_email(db, user_data.email)
        if existing_user:
            logger.warning(f"Email already exists: {user_data.email}")
            raise EmailAlreadyExists()
        
        # Check if username already exists
        existing_username = user_crud.get_user_by_username(db, user_data.username)
        if existing_username:
            logger.warning(f"Username already exists: {user_data.username}")
            raise EmailAlreadyExists("Username already exists")
        
        # Create user
        user = user_crud.create_user(db, user_data)
        
        # Assign default role (employee)
        default_role = role_crud.get_role_by_name(db, "employee")
        if default_role:
            user_crud.assign_role(db, user.id, default_role.id)
        
        logger.info(f"User registered successfully: {user.email}")
        return user
    
    @staticmethod
    def login(db: Session, login_data: LoginRequest):
        """Login user"""
        logger.info(f"Login attempt: {login_data.email}")
        
        # Get user by email
        user = user_crud.get_user_by_email(db, login_data.email)
        if not user:
            logger.warning(f"User not found: {login_data.email}")
            raise InvalidCredentials()
        
        # Verify password
        if not verify_password(login_data.password, user.hashed_password):
            logger.warning(f"Invalid password for user: {login_data.email}")
            raise InvalidCredentials()
        
        # Check if user is active
        if not user.is_active:
            logger.warning(f"Inactive user login attempt: {login_data.email}")
            raise InvalidCredentials("User account is inactive")
        
        # Get user role
        role_name = user.roles[0].name if user.roles else "employee"
        
        # Create tokens
        token_data = {
            "user_id": user.id,
            "email": user.email,
            "role": role_name
        }
        
        access_token = create_access_token(token_data)
        refresh_token = create_refresh_token(token_data)
        
        logger.info(f"User logged in successfully: {user.email}")
        
        return {
            "user": user,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60
        }
    
    @staticmethod
    def refresh_access_token(refresh_token: str):
        """Refresh access token"""
        logger.info("Refreshing access token")
        
        token_data = verify_token(refresh_token)
        if not token_data:
            logger.warning("Invalid refresh token")
            raise InvalidCredentials("Invalid refresh token")
        
        # Create new access token
        new_token_data = {
            "user_id": token_data.user_id,
            "email": token_data.email,
            "role": token_data.role
        }
        
        access_token = create_access_token(new_token_data)
        
        logger.info(f"Access token refreshed for user: {token_data.email}")
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60
        }
    
    @staticmethod
    def change_password(db: Session, user_id: int, old_password: str, new_password: str):
        """Change user password"""
        logger.info(f"Changing password for user ID: {user_id}")
        
        user = user_crud.get_user_by_id(db, user_id)
        if not user:
            logger.warning(f"User not found: {user_id}")
            raise UserNotFound()
        
        # Verify old password
        if not verify_password(old_password, user.hashed_password):
            logger.warning(f"Invalid old password for user: {user_id}")
            raise InvalidCredentials("Invalid old password")
        
        # Update password
        hashed_password = get_password_hash(new_password)
        user_crud.update_user(db, user_id, hashed_password=hashed_password)
        
        logger.info(f"Password changed successfully for user: {user_id}")
        return True

class RoleService:
    @staticmethod
    def create_role(db: Session, name: str, description: str = None, permission_ids: list = None):
        """Create a new role"""
        logger.info(f"Creating role: {name}")
        
        # Check if role already exists
        existing_role = role_crud.get_role_by_name(db, name)
        if existing_role:
            logger.warning(f"Role already exists: {name}")
            raise EmailAlreadyExists(f"Role '{name}' already exists")
        
        # Create role
        role = role_crud.create_role(db, name, description)
        
        # Assign permissions
        if permission_ids:
            for permission_id in permission_ids:
                role_crud.assign_permission(db, role.id, permission_id)
        
        logger.info(f"Role created successfully: {name}")
        return role
    
    @staticmethod
    def get_all_roles(db: Session):
        """Get all roles"""
        logger.info("Fetching all roles")
        return role_crud.get_all_roles(db)
    
    @staticmethod
    def assign_role_to_user(db: Session, user_id: int, role_id: int):
        """Assign role to user"""
        logger.info(f"Assigning role {role_id} to user {user_id}")
        
        user = user_crud.get_user_by_id(db, user_id)
        if not user:
            logger.warning(f"User not found: {user_id}")
            raise UserNotFound()
        
        success = user_crud.assign_role(db, user_id, role_id)
        if not success:
            logger.warning(f"Failed to assign role {role_id} to user {user_id}")
            raise EmailAlreadyExists("Failed to assign role")
        
        logger.info(f"Role assigned successfully to user: {user_id}")
        return True

class PermissionService:
    @staticmethod
    def create_permission(db: Session, name: str, description: str = None, category: str = None):
        """Create a new permission"""
        logger.info(f"Creating permission: {name}")
        
        # Check if permission already exists
        existing_permission = permission_crud.get_permission_by_name(db, name)
        if existing_permission:
            logger.warning(f"Permission already exists: {name}")
            raise EmailAlreadyExists(f"Permission '{name}' already exists")
        
        # Create permission
        permission = permission_crud.create_permission(db, name, description, category)
        
        logger.info(f"Permission created successfully: {name}")
        return permission
    
    @staticmethod
    def get_all_permissions(db: Session):
        """Get all permissions"""
        logger.info("Fetching all permissions")
        return permission_crud.get_all_permissions(db)
