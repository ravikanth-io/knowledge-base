from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.note import Note
from app.schemas.note_schema import NoteCreate
from app.services.search_engine import SearchEngine

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/notes")
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = Note(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@router.get("/notes")
def get_notes(db: Session = Depends(get_db)):
    return db.query(Note).all()

@router.get("/search")
def search(query: str, db: Session = Depends(get_db)):
    notes = db.query(Note).all()
    engine = SearchEngine(notes)
    return engine.search(query)