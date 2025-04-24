from sqlalchemy.orm import Session
from typing import Optional
from . import models, schemas


def get_contents(db: Session, skip: int = 0, limit: int = 100, featured: Optional[bool] = None):
    query = db.query(models.Content)
    if featured is not None:
        query = query.filter(models.Content.featured == featured)
    return query.offset(skip).limit(limit).all()


def get_content(db: Session, content_id: int):
    return db.query(models.Content).filter(models.Content.id == content_id).first()


def create_content(db: Session, content: schemas.ContentCreate):
    db_content = models.Content(**content.dict())
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content


def update_content(db: Session, content_id: int, content: schemas.ContentCreate):
    db_content = db.query(models.Content).filter(models.Content.id == content_id).first()
    if not db_content:
        return None
    for field, value in content.dict(exclude_unset=True).items():
        setattr(db_content, field, value)
    db.commit()
    db.refresh(db_content)
    return db_content


def delete_content(db: Session, content_id: int):
    db_content = db.query(models.Content).filter(models.Content.id == content_id).first()
    if not db_content:
        return None
    db.delete(db_content)
    db.commit()
    return db_content
