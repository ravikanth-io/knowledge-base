from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi import FastAPI
from app.routes.notes import router as notes_router
from app.auth.routes import router as auth_router

app = FastAPI()

app.include_router(notes_router)
app.include_router(auth_router)
port = int(os.environ.get("PORT", 10000))

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
