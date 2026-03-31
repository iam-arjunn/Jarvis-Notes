from pydantic import BaseModel
from typing import Optional

class NoteCreate(BaseModel):
    title: str
    content: Optional[str] = None
    subject: Optional[str] = None

class NoteUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
    subject: Optional[str]