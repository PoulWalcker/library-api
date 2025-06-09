from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import UserCreate, UserUpdate, UserRead
from app.crud import create_user, get_user_by_id, update_user, remove_user

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserRead)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(user, db)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserRead)
def edit_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    user = update_user(user_id, user_data, db)
    db.commit()
    db.refresh(user)
    return user


@router.delete("/{user_id}", response_model=UserRead)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = remove_user(user_id, db)
    db.commit()
    return user
