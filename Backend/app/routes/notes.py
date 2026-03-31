from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.schemas.note_schema import NoteCreate
from app.models.note_model import Note
from app.db.database import get_db

router = APIRouter()

@router.post("/notes")
def create_note(note: NoteCreate, db: Session = Depends(get_db)):

    new_note = Note(
        title=note.title,
        content=note.content,
        subject=note.subject,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return {"message": "Note created", "id": str(new_note.id)}


@router.get("/notes")
def get_notes(db: Session = Depends(get_db)):
    return db.query(Note).all()