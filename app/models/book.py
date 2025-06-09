from sqlalchemy import Column, Integer, String, Date
from .base import Base

from pydantic import BaseModel
from datetime import date
from typing import Optional


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publication_date = Column(Date, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
    amount = Column(Integer, default=1)


class BookCreate(BaseModel):
    title: str
    author: str
    publication_date: date
    isbn: str
    amount: int = 1


class BookRead(BaseModel):
    id: int
    title: str
    author: str
    publication_date: date
    isbn: str
    amount: int

    class Config:
        orm_mode = True


class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    publication_date: Optional[date]
    isbn: Optional[str]
    amount: Optional[int]
