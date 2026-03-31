from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.note_tag_model import NoteTag
from app.schemas.note_tag_schema import NoteTagCreate
from app.models.note_model import Note
from app.models.tag_model import Tag

router = APIRouter()

@router.post("/note-tags")
def add_tag_to_note(data: NoteTagCreate, db: Session = Depends(get_db)):

    note = db.query(Note).filter(Note.id == data.note_id).first()
    tag = db.query(Tag).filter(Tag.id == data.tag_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    nt = NoteTag(note_id=data.note_id, tag_id=data.tag_id)
    db.add(nt)
    db.commit()
    return nt


@router.get("/note-tags/{note_id}")
def get_tags_of_note(note_id: str, db: Session = Depends(get_db)):
    return db.query(NoteTag).filter(NoteTag.note_id == note_id).all()