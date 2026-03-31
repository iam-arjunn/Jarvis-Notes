from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.db.database import get_db
from app.models.note_model import Note
from app.schemas.note_schema import NoteCreate, NoteUpdate

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
    return new_note


@router.get("/notes")
def get_notes(db: Session = Depends(get_db)):
    return db.query(Note).filter(Note.is_deleted == False).all()


@router.get("/notes/{note_id}")
def get_note(note_id: str, db: Session = Depends(get_db)):
    return db.query(Note).filter(Note.id == note_id).first()


@router.put("/notes/{note_id}")
def update_note(note_id: str, data: NoteUpdate, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()

    if data.title:
        note.title = data.title
    if data.content:
        note.content = data.content
    if data.subject:
        note.subject = data.subject

    note.updated_at = datetime.utcnow()

    db.commit()
    return note


@router.delete("/notes/{note_id}")
def delete_note(note_id: str, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    note.is_deleted = True
    db.commit()
    return {"message": "Deleted"}