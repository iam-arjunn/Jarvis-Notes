from pydantic import BaseModel

class NoteTagCreate(BaseModel):
    note_id: str
    tag_id: str