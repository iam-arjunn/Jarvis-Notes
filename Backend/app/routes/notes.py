from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from app.db.database import get_db
from app.models.note_model import Note
from app.schemas.note_schema import NoteCreate, NoteUpdate
from app.core.dependencies import get_current_user  

router = APIRouter()

@router.post("/notes")
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)  
):
    new_note = Note(
        title=note.title,
        content=note.content,
        subject=note.subject,
        user_id=user.id,  
        created_at = datetime.now(timezone.utc),
        updated_at = datetime.now(timezone.utc)
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


@router.get("/notes")
def get_notes(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)  
):
    return db.query(Note).filter(
        Note.user_id == user.id,   
        Note.is_deleted == False
    ).all()


@router.get("/notes/{note_id}")
def get_note(
    note_id: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)  
):
    note = db.query(Note).filter(
        Note.id == note_id,
        Note.user_id == user.id
    ).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    return note


@router.put("/notes/{note_id}")
def update_note(
    note_id: str,
    data: NoteUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)  
):
    note = db.query(Note).filter(
        Note.id == note_id,
        Note.user_id == user.id
    ).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

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
def delete_note(
    note_id: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    note = db.query(Note).filter(
        Note.id == note_id,
        Note.user_id == user.id
    ).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    note.is_deleted = True
    db.commit()
    return {"message": "Deleted"}