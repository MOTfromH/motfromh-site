# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import Base
from app.routes import content

app = FastAPI()

# 🔐 CORS-Einstellungen
origins = [
    "http://localhost:3000",  # dein lokales Frontend
    "http://127.0.0.1:3000",
    # "https://deine-domain.tld",  # später für Produktion
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"status": "ok"}

app.include_router(content.router)
