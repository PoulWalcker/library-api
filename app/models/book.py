from sqlalchemy import Column, Integer, String, Date
from base import Base


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publication_date = Column(Date, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
    amount = Column(Integer, default=1)
