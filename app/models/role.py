from .base import Base
from sqlalchemy import Column, Integer, String

from pydantic import BaseModel
from typing import Optional


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)


class RoleCreate(BaseModel):
    name: str


class RoleRead(BaseModel):
    name: str

    class Config:
        orm_mode = True


class RoleUpdate(BaseModel):
    name: str
