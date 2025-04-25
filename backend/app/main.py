# app/main.py
from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import content

app = FastAPI()

@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"status": "ok"}

app.include_router(content.router)
