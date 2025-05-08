from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, crud
from ..database import get_db

router = APIRouter(
    prefix="/content",
    tags=["Content"]
)

@router.get("/", response_model=List[schemas.Content])
def get_all_content(db: Session = Depends(get_db)):
    return crud.get_contents(db)

@router.get("/new/", response_model=List[schemas.Content])
def newest_content(db: Session = Depends(get_db)):
    return crud.get_contents(db=db, limit=3)

@router.get("/featured/", response_model=List[schemas.Content])
def get_featured_content(db: Session = Depends(get_db)):
    return crud.get_contents(db, featured=True)

@router.get("/{id}/", response_model=schemas.Content)
def get_content(id: int, db: Session = Depends(get_db)):
    entry = crud.get_content(db, content_id=id)
    if not entry:
        raise HTTPException(status_code=404, detail="Content not found")
    if not entry.has_view:
        raise HTTPException(status_code=403, detail="No view available")
    return entry

@router.post("/", response_model=schemas.Content)
def create_content(content: schemas.ContentCreate, db: Session = Depends(get_db)):
    return crud.create_content(db=db, content=content)

@router.delete("/{id}/", response_model=schemas.Content)
def delete_content(id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_content(db=db, content_id=id)    
    if not deleted: 
        raise HTTPException(status_code=404, detail="Content not found")
    return deleted

@router.put("/{id}/", response_model=schemas.Content)
def update_content(id: int, content: schemas.ContentCreate, db: Session = Depends(get_db)):
    updated = crud.update_content(db=db, content_id=id, content=content)
    if not updated:
        raise HTTPException(status_code=404, detail="Content not found")
    return updated
