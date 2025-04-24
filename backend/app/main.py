from fastapi import FastAPI
from app.routes import content

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "ok"}

app.include_router(content.router)
