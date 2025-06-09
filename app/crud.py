from sqlalchemy import select
from app.models.book import Book, BookCreate, BookUpdate
from app.models.user import User, UserCreate, UserUpdate
from app.models.role import Role, RoleCreate, RoleUpdate
from app.models.borrowed_book import BorrowedBook


# ----- Book -----

def create_book(book: BookCreate, session):
    existing_book = session.scalar(select(Book).where(Book.isbn == book.isbn))
    if existing_book:
        raise ValueError(f"Book with ISBN {book.isbn} already exists")

    db_book = Book(**book.dict())
    session.add(db_book)
    return db_book


def get_book_by_id(book_id: int, session):
    statement = select(Book).where(Book.id == book_id)
    return session.scalars(statement).one()


def update_book(book_id: int, book_data: BookUpdate, session):
    db_book = get_book_by_id(book_id, session)
    for key, value in book_data.dict(exclude_unset=True).items():
        setattr(db_book, key, value)
    return db_book


def remove_book_by_id(book_id: int, session):
    db_book = get_book_by_id(book_id, session)
    session.delete(db_book)
    return db_book


# ----- Borrowed Book -----

def create_borrowed_book(borrowed_book: BorrowedBook, session):
    session.add(borrowed_book)
    return borrowed_book


def get_borrowed_book_by_id(bbook_id: int, session):
    statement = select(BorrowedBook).where(BorrowedBook.id == bbook_id)
    return session.scalars(statement).one()


def update_borrowed_book(bbook_id: int, borrowed_book_data: dict, session):
    db_object = get_borrowed_book_by_id(bbook_id, session)
    for key, value in borrowed_book_data.items():
        setattr(db_object, key, value)
    return db_object


def remove_borrowed_book_by_id(bbook_id: int, session):
    db_object = get_borrowed_book_by_id(bbook_id, session)
    session.delete(db_object)
    return db_object


# ----- User -----

def create_user(user: UserCreate, session):
    existing_user = session.scalar(select(User).where(User.email == user.email))
    if existing_user:
        raise ValueError(f"User with email {user.email} already exists")

    db_user = User(**user.dict())
    session.add(db_user)
    return db_user


def get_user_by_id(user_id: int, session):
    statement = select(User).where(User.id == user_id)
    return session.scalars(statement).one()


def update_user(user_id: int, user_data: UserUpdate, session):
    db_user = get_user_by_id(user_id, session)
    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    return db_user


def remove_user(user_id: int, session):
    db_user = get_user_by_id(user_id, session)
    session.delete(db_user)
    return db_user


# ----- Role -----

def create_role(role: RoleCreate, session):
    existing_role = session.scalar(select(Role).where(Role.name == role.name))
    if existing_role:
        raise ValueError(f"Role with name {role.name} already exists")

    db_role = Role(**role.dict())
    session.add(db_role)
    return db_role


def get_role_by_id(role_id: int, session):
    statement = select(Role).where(Role.id == role_id)
    return session.scalars(statement).one()


def update_role(role_id: int, role_data: RoleUpdate, session):
    db_role = get_role_by_id(role_id, session)
    for key, value in role_data.dict(exclude_unset=True).items():
        setattr(db_role, key, value)
    return db_role


def remove_role(role_id: int, session):
    db_role = get_role_by_id(role_id, session)
    session.delete(db_role)
    return db_role
