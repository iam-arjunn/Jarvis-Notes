from pydantic import BaseModel
from uuid import UUID

class NoteTagCreate(BaseModel):
    note_id: UUID
    tag_id: UUID