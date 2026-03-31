from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.tag_model import Tag
from app.schemas.tag_schema import TagCreate

router = APIRouter()

@router.post("/tags")
def create_tag(data: TagCreate, db: Session = Depends(get_db)):
    tag = Tag(name=data.name)
    db.add(tag)
    db.commit()
    return tag


@router.get("/tags")
def get_tags(db: Session = Depends(get_db)):
    return db.query(Tag).all()