from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware
import os

port = int(os.environ.get("PORT", 10000))
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Knowledge Base API Running"}