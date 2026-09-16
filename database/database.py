from sqlite3 import DatabaseError
from sqlalchemy import create_engine, false
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# CREATE DATABASE TO STORE API DATA

DATABASE_URL = "sqlite:///mission_control.db"

class Base(DeclarativeBase):
    pass

engine = create_engine(
    DATABASE_URL,
    echo=False
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)
