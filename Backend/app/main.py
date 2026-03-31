from fastapi import FastAPI
from app.routes import notes, attachments, tags, note_tags, auth

app = FastAPI()

app.include_router(notes.router, tags=["Notes"])
app.include_router(attachments.router, tags=["Attachments"])
app.include_router(tags.router, tags=["Tags"])
app.include_router(note_tags.router, tags=["Note Tags"])
app.include_router(auth.router, tags=["Authentication"])