from .base import Base
from .role import Role
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(35), nullable=False, unique=False)
    email = Column(String, nullable=False, unique=True)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)

    role = relationship('Role')
