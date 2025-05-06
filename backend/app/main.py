# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import Base
from app.routes import content
from app import seeds

app = FastAPI()
@app.on_event("startup")
def create_tables():
    for i in range(10):             # bis zu 10 Versuche
        try:
            Base.metadata.create_all(bind=engine)
            break                   # bei Erfolg raus
        except OperationalError:
            print("DB noch nicht bereit, warte 1s…")
            time.sleep(1)
    else:
        raise RuntimeError("Konnte nach 10 Versuchen keine DB-Verbindung herstellen")

seeds.seed_db()

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


@app.get("/")
async def root():
    return {"status": "ok"}

app.include_router(content.router)
