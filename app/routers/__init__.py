from fastapi import APIRouter

from .user import router as user_router
from .book import router as book_router
from .borrowed_book import router as borrowed_book_router

api_router = APIRouter()

api_router.include_router(user_router)
api_router.include_router(book_router)
api_router.include_router(borrowed_book_router)
