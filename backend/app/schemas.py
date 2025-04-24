from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ContentCreate(BaseModel):
    title: str
    description: Optional[str] = None
    body: Optional[str] = None
    image_url: Optional[str] = None
    gallery: Optional[list[str]] = None
    links: Optional[dict] = None

class Content(ContentCreate): 
    id: int	
    created_at: datetime
    

    class Config:
        from_attributes = True