from .base import Base
from .role import Role
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from pydantic import BaseModel, EmailStr
from typing import Optional


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(35), nullable=False, unique=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String,nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)

    role = relationship('Role')


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Optional[str] = 'Reader'


class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    role: Optional[str]
