from enum import Enum

from pydantic import BaseModel, EmailStr, Field


class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"


class UserRequest(BaseModel):
    username: str = Field(description="Username")
    email: EmailStr = Field(description="Email address")
    password: str = Field(min_length=8, description="Password")
    status: bool = Field(default=True)
    role: str = Field(default=UserRole.USER)


class UserResponse(BaseModel):
    id: int
    role: str
    email: EmailStr
    status: bool
