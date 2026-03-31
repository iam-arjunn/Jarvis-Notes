from fastapi import FastAPI
from app.routes import notes, attachments, tags, note_tags

app = FastAPI()

app.include_router(notes.router)
app.include_router(attachments.router)
app.include_router(tags.router)
app.include_router(note_tags.router)