from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.note import Note
from app.dependencies import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@router.post("/notes")
def create_note(data: dict, db: Session = Depends(get_db), user=Depends(get_current_user)):
    note = Note(title=data["title"], content=data["content"])
    db.add(note)
    db.commit()
    return {"msg": "created"}

# READ
@router.get("/notes")
def get_notes(db: Session = Depends(get_db)):
    return db.query(Note).all()

# UPDATE
@router.put("/notes/{note_id}")
def update_note(note_id: int, data: dict, db: Session = Depends(get_db), user=Depends(get_current_user)):
    note = db.query(Note).filter(Note.id == note_id).first()
    note.title = data["title"]
    note.content = data["content"]
    db.commit()
    return {"msg": "updated"}

# DELETE
@router.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    note = db.query(Note).filter(Note.id == note_id).first()
    db.delete(note)
    db.commit()
    return {"msg": "deleted"}
