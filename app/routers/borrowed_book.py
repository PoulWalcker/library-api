from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.borrowed_book import BorrowedBook
from app.models.borrowed_book import BorrowedBookCreate, BorrowedBookRead
from app.crud import create_borrowed_book, get_borrowed_book_by_id, update_borrowed_book, remove_borrowed_book_by_id

router = APIRouter(prefix="/borrowed_books", tags=["borrowed_books"])


@router.post("/", response_model=BorrowedBookRead)
def add_borrowed_book(borrowed_book: BorrowedBookCreate, db: Session = Depends(get_db)):
    db_book = create_borrowed_book(BorrowedBook(**borrowed_book.dict()), db)
    db.commit()
    return db_book


@router.get("/{bbook_id}", response_model=BorrowedBookRead)
def read_borrowed_book(bbook_id: int, db: Session = Depends(get_db)):
    book = get_borrowed_book_by_id(bbook_id, db)
    if not book:
        raise HTTPException(status_code=404, detail="Borrowed book not found")
    return book


@router.put("/{bbook_id}", response_model=BorrowedBookRead)
def edit_borrowed_book(bbook_id: int, borrowed_book_data: BorrowedBookCreate, db: Session = Depends(get_db)):
    book = update_borrowed_book(bbook_id, borrowed_book_data.dict(), db)  # .dict() здесь
    db.commit()
    return book



@router.delete("/{bbook_id}")
def delete_borrowed_book(bbook_id: int, db: Session = Depends(get_db)):
    book = remove_borrowed_book_by_id(bbook_id, db)
    db.commit()
    return book
