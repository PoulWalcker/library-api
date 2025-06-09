from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base
from config import settings


from app.models.user import User
from app.models.book import Book
from app.models.borrowed_book import BorrowedBook
from app.models.role import Role


DATABASE_URL = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Create tables
def init_db():
    Base.metadata.create_all(bind=engine)
