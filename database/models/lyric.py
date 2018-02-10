from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
import datetime

from ..database import Base
from .crud import CRUD


class Lyric(Base, CRUD):
    __tablename__ = 'lyrics'

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, nullable=False, unique=True)
    datetime = Column(DateTime)
    text = Column(String(1024), nullable=False)
    rating = Column(Integer)
    deleted = Column(Boolean)

    def __init__(self, text=None):
        self.id = None
        self.datetime = datetime.datetime.now()
        self.text = text
        self.rating = 0
        self.deleted = False
