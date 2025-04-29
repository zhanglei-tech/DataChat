from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreateSchema(BaseModel):
    """用户创建校验模型"""
    username: str
    password: str
    email: Optional[EmailStr] = None

class UserLoginSchema(BaseModel):
    """用户登录校验模型"""
    username: str
    password: str

class UserSchema(BaseModel):
    """用户基础数据模型"""
    id: int
    username: str
    email: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True

class UserResponseSchema(BaseModel):
    """用户响应模型"""
    id: int
    username: str
    email: Optional[str]
    created_at: str

    class Config:
        from_attributes = True