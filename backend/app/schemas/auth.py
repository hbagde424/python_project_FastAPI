from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import List, Optional

# Request schemas
class RegisterRequest(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    full_name: str = Field(..., min_length=1, max_length=100)
    password: str = Field(..., min_length=8)
    confirm_password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class RefreshTokenRequest(BaseModel):
    refresh_token: str

# Response schemas
class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int

class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    full_name: str
    is_active: bool
    is_verified: bool
    created_at: datetime
    roles: List['RoleResponse'] = []
    
    class Config:
        from_attributes = True

class RoleResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    permissions: List['PermissionResponse'] = []
    
    class Config:
        from_attributes = True

class PermissionResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    category: Optional[str]
    
    class Config:
        from_attributes = True

class LoginResponse(BaseModel):
    user: UserResponse
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str = Field(..., min_length=8)
    confirm_password: str

class AssignRoleRequest(BaseModel):
    user_id: int
    role_id: int

class CreateRoleRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    description: Optional[str] = None
    permission_ids: List[int] = []

class CreatePermissionRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    category: Optional[str] = None
