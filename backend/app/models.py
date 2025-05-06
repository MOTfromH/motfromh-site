from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from datetime import datetime
from sqlalchemy.dialects.postgresql import ARRAY, JSON

from .database import Base

class Content(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)                  # Titel für Card & View
    description = Column(Text)                              # Vorschau-Text
    body = Column(Text, nullable=True)                      # Optionaler längerer Text (View)
    image_url = Column(String, nullable=True)               # z. B. /static/images/foo.png
    gallery = Column(ARRAY(String), nullable=True)          # Mehrere Bildpfade
    links = Column(JSON, nullable=True)                     # {"github": "...", "demo": "..."}
    has_view = Column(Boolean, default=False)               # ob es eine View-Seite gibt
    created_at = Column(DateTime, default=datetime.utcnow)  