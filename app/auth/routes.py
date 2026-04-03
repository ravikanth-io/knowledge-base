from fastapi import APIRouter, HTTPException
from app.auth.auth import create_access_token

router = APIRouter()

# simple static login (for demo)
USERNAME = "admin"
PASSWORD = "1234"

@router.post("/login")
def login(data: dict):
    if data["username"] == USERNAME and data["password"] == PASSWORD:
        token = create_access_token({"user": data["username"]})
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")
