from typing import Literal
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    role: Literal["user", "admin"] = "user"  # Default role is 'user'

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    role: str

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    email: str | None = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str