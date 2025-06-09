from sqlalchemy import select

from app.models.base import Base
from app.models.borrowed_book import BorrowedBook
from app.models.book import Book
from app.models.user import User
from app.models.role import Role


# ----- Book -----
def create_book(book: Book, session):
    statement = select(Book).where(Book.isbn == book.isbn)  # type: ignore
    existing_book = session.scalars(statement).first()
    if existing_book:
        raise ValueError(f"Book with ISBN {book.isbn} already exists")

    session.add(book)


def get_book_by_id(book_id: int, session):
    statement = select(Book).where(Book.id == book_id)
    db_object = session.scalars(statement).one()
    return db_object


def update_book(new_object: Book, session):
    session.merge(new_object)


def remove_book_by_id(book_id: int, session):
    statement = select(Book).where(Book.id == book_id)
    db_object = session.scalars(statement).one()

    session.delete(db_object)
    return db_object


# ----- Borrowed Book -----
def create_borrowed_book(book: BorrowedBook, session):
    session.add(book)


def get_borrowed_book_by_id(bbook_id: int, session):
    statement = select(BorrowedBook).where(BorrowedBook.id == bbook_id)
    db_object = session.scalars(statement).one()
    return db_object


def update_borrowed_book(new_object: BorrowedBook, session):
    session.merge(new_object)


def remove_borrowed_book_by_id(bbook_id: int, session):
    statement = select(BorrowedBook).where(BorrowedBook.id == bbook_id)
    db_object = session.scalars(statement).one()

    session.delete(db_object)
    return db_object


# ----- User -----
def create_user(user: User, session):
    statement = select(User).where(User.email == user.email)  # type: ignore
    existing_user = session.scalar(statement)
    if existing_user:
        raise ValueError(f"User with email {user.email} already exists")

    session.add(user)


def get_user_by_id(user_id: int, session):
    statement = select(User).where(User.id == user_id)
    db_object = session.scalars(statement).one()
    return db_object


def update_user(new_object: User, session):
    session.merge(new_object)


def remove_user(user_id: int, session):
    statement = select(User).where(User.id == user_id)
    db_object = session.scalars(statement).one()

    session.delete(db_object)
    return db_object


# ----- Role -----
def create_role(role: Role, session):
    statement = select(Role).where(Role.name == user.name)  # type: ignore
    existing_role = session.scalar(statement)
    if existing_role:
        raise ValueError(f"Role with name {role.name} already exists")

    session.add(role)


def get_role_by_id(role_id: int, session):
    statement = select(Role).where(Role.id == role_id)
    db_object = session.scalars(statement).one()
    return db_object


def update_role(new_object: Role, session):
    session.merge(new_object)


def remove_role(role_id: int, session):
    statement = select(Role).where(Role.id == role_id)
    db_object = session.scalars(statement).one()

    session.delete(db_object)
    return db_object
