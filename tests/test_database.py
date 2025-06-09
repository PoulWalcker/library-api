from app.database import SessionLocal, engine
from app.models.base import Base
from sqlalchemy import text


def test_db_connection():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        result = db.execute(text('SELECT 1 ')).fetchall()
        assert result == [(1,)]
    finally:
        db.close()


test_db_connection()
