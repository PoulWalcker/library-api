from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.book import BookCreate, BookUpdate, BookRead
from app.crud import create_book, get_book_by_id, update_book, remove_book_by_id

router = APIRouter(prefix="/books", tags=["books"])


@router.post("/", response_model=BookRead)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = create_book(book, db)
    db.commit()
    db.refresh(db_book)
    return db_book


@router.get("/{book_id}", response_model=BookRead)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = get_book_by_id(book_id, db)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/{book_id}", response_model=BookRead)
def edit_book(book_id: int, book_data: BookUpdate, db: Session = Depends(get_db)):
    book = update_book(book_id, book_data, db)
    db.commit()
    db.refresh(book)
    return book


@router.delete("/{book_id}", response_model=BookRead)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = remove_book_by_id(book_id, db)
    db.commit()
    return book
