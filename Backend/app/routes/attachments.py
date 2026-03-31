from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.db.database import get_db
from app.models.attachment_model import Attachment
from app.schemas.attachment_schema import AttachmentCreate

router = APIRouter()

@router.post("/attachments")
def add_attachment(data: AttachmentCreate, db: Session = Depends(get_db)):
    att = Attachment(
        note_id=data.note_id,
        file_url=data.file_url,
        file_type=data.file_type,
        file_name=data.file_name,
        created_at=datetime.utcnow()
    )
    db.add(att)
    db.commit()
    return att


@router.get("/attachments/{note_id}")
def get_attachments(note_id: str, db: Session = Depends(get_db)):
    return db.query(Attachment).filter(Attachment.note_id == note_id).all()