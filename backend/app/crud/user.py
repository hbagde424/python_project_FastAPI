from sqlalchemy.orm import Session
from app.models.user import User, Role, Permission
from app.schemas.auth import RegisterRequest
from app.core.security import get_password_hash
from typing import Optional, List

class UserCRUD:
    @staticmethod
    def create_user(db: Session, user_data: RegisterRequest) -> User:
        """Create a new user"""
        db_user = User(
            email=user_data.email,
            username=user_data.username,
            full_name=user_data.full_name,
            hashed_password=get_password_hash(user_data.password)
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[User]:
        """Get user by email"""
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def get_user_by_username(db: Session, username: str) -> Optional[User]:
        """Get user by username"""
        return db.query(User).filter(User.username == username).first()
    
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
        """Get user by ID"""
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_all_users(db: Session, skip: int = 0, limit: int = 10) -> List[User]:
        """Get all users"""
        return db.query(User).offset(skip).limit(limit).all()
    
    @staticmethod
    def update_user(db: Session, user_id: int, **kwargs) -> Optional[User]:
        """Update user"""
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            db.commit()
            db.refresh(user)
        return user
    
    @staticmethod
    def assign_role(db: Session, user_id: int, role_id: int) -> bool:
        """Assign role to user"""
        user = db.query(User).filter(User.id == user_id).first()
        role = db.query(Role).filter(Role.id == role_id).first()
        
        if user and role:
            if role not in user.roles:
                user.roles.append(role)
                db.commit()
            return True
        return False
    
    @staticmethod
    def remove_role(db: Session, user_id: int, role_id: int) -> bool:
        """Remove role from user"""
        user = db.query(User).filter(User.id == user_id).first()
        role = db.query(Role).filter(Role.id == role_id).first()
        
        if user and role and role in user.roles:
            user.roles.remove(role)
            db.commit()
            return True
        return False

class RoleCRUD:
    @staticmethod
    def create_role(db: Session, name: str, description: str = None) -> Role:
        """Create a new role"""
        db_role = Role(name=name, description=description)
        db.add(db_role)
        db.commit()
        db.refresh(db_role)
        return db_role
    
    @staticmethod
    def get_role_by_id(db: Session, role_id: int) -> Optional[Role]:
        """Get role by ID"""
        return db.query(Role).filter(Role.id == role_id).first()
    
    @staticmethod
    def get_role_by_name(db: Session, name: str) -> Optional[Role]:
        """Get role by name"""
        return db.query(Role).filter(Role.name == name).first()
    
    @staticmethod
    def get_all_roles(db: Session) -> List[Role]:
        """Get all roles"""
        return db.query(Role).all()
    
    @staticmethod
    def assign_permission(db: Session, role_id: int, permission_id: int) -> bool:
        """Assign permission to role"""
        role = db.query(Role).filter(Role.id == role_id).first()
        permission = db.query(Permission).filter(Permission.id == permission_id).first()
        
        if role and permission:
            if permission not in role.permissions:
                role.permissions.append(permission)
                db.commit()
            return True
        return False

class PermissionCRUD:
    @staticmethod
    def create_permission(db: Session, name: str, description: str = None, category: str = None) -> Permission:
        """Create a new permission"""
        db_permission = Permission(name=name, description=description, category=category)
        db.add(db_permission)
        db.commit()
        db.refresh(db_permission)
        return db_permission
    
    @staticmethod
    def get_permission_by_id(db: Session, permission_id: int) -> Optional[Permission]:
        """Get permission by ID"""
        return db.query(Permission).filter(Permission.id == permission_id).first()
    
    @staticmethod
    def get_permission_by_name(db: Session, name: str) -> Optional[Permission]:
        """Get permission by name"""
        return db.query(Permission).filter(Permission.name == name).first()
    
    @staticmethod
    def get_all_permissions(db: Session) -> List[Permission]:
        """Get all permissions"""
        return db.query(Permission).all()

user_crud = UserCRUD()
role_crud = RoleCRUD()
permission_crud = PermissionCRUD()
