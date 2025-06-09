from fastapi import FastAPI
from app.routers import api_router
from app.database import init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()


app.include_router(api_router)
