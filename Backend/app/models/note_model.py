from sqlalchemy import Column, Text, Boolean, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
import uuid

Base = declarative_base()

class Note(Base):
    __tablename__ = "notes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True))
    title = Column(Text)
    content = Column(Text)
    subject = Column(Text)
    is_pinned = Column(Boolean, default=False)
    is_archived = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)