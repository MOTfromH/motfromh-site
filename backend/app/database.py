from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from dotenv import load_dotenv
import os

load_dotenv()

api = os.getenv("DATABASE_URL")

engine = create_engine(
    api,                  # DATABASE_URL
    pool_pre_ping=True,   # optional: prevent stale connections
    connect_args={
        "connect_timeout": 5  # optional: Time-out for initial TCP-Connect
    }
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()