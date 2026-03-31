from pydantic import BaseModel
from typing import Optional

class NoteCreate(BaseModel):
    title: str
    content: Optional[str] = None
    subject: Optional[str] = None