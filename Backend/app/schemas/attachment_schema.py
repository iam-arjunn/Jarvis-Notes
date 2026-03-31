from pydantic import BaseModel

class AttachmentCreate(BaseModel):
    note_id: str
    file_url: str
    file_type: str
    file_name: str