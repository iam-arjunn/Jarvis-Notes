from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.note_tag_model import NoteTag
from app.schemas.note_tag_schema import NoteTagCreate

router = APIRouter()

@router.post("/note-tags")
def add_tag_to_note(data: NoteTagCreate, db: Session = Depends(get_db)):
    nt = NoteTag(note_id=data.note_id, tag_id=data.tag_id)
    db.add(nt)
    db.commit()
    return nt


@router.get("/note-tags/{note_id}")
def get_tags_of_note(note_id: str, db: Session = Depends(get_db)):
    return db.query(NoteTag).filter(NoteTag.note_id == note_id).all()