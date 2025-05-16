from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import OperationalError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import time
from app.database import engine, SessionLocal
from app.models import Base
from app.routes import content, test
from app import seeds

app = FastAPI()
@app.on_event("startup")
def create_tables():
    for i in range(10):             # 10 trys
        try:
            Base.metadata.create_all(bind=engine)
            break                   
        except OperationalError:
            print("DB is not ready, please wait 1s…")
            time.sleep(1)
    else:
        raise RuntimeError("could not connect to DB after 10 attempts")

# Create testdata from seeds at startup
@app.on_event("startup")
def on_startup():
    
    db = SessionLocal()
    try:
        seeds.seed_db(db)
    finally:
        db.close()
        
# Add In-Memory-Testdata if needed   
#    test.seed_test_data()

# CORS-Config
origins = [
    "http://localhost:5173",  # local frontend
    "http://127.0.0.1:5173",
   # "https://deine-domain.tld",  # production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/")
async def root():
    return {"status": "ok"}

@app.get("/test/")
async def root():
    return {"status": "test ok"}

app.include_router(content.router, prefix="/api/v1")

# Test-Router
# app.include_router(test.router, prefix="/test")