from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

from pydantic import BaseModel
from datetime import date
from typing import Optional


class BorrowedBook(Base):
    __tablename__ = 'borrowed_books'
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    reader_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    borrow_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)

    book = relationship("Book")
    reader = relationship("User")


class BorrowedBookCreate(BaseModel):
    book_id: int
    reader_id: int
    borrow_date: date
    return_date: Optional[date] = None


class BorrowedBookRead(BaseModel):
    id: int
    book_id: int
    reader_id: int
    borrow_date: date
    return_date: Optional[date]

    class Config:
        from_attributes = True


class BorrowedBookUpdate(BaseModel):
    return_date: Optional[date]
