from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    class Config:
        env_file = str(Path(__file__).parent / ".env")


settings = Settings()
