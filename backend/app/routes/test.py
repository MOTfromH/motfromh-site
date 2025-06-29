from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/test", tags=["test"])

# 1) Schema & Model
class TestEntry(BaseModel):
    id: int
    title: str
    description: str

# 2) In-Memory „Model“
_test_store: List[TestEntry] = []

# 3) CRUD-Logic
@router.get("/", response_model=List[TestEntry])
def list_entries():
    return _test_store

@router.post("/", response_model=TestEntry, status_code=201)
def create_entry(entry: TestEntry):
    if any(e.id == entry.id for e in _test_store):
        raise HTTPException(400, "ID already exists")
    _test_store.append(entry)
    return entry

@router.delete("/{id}/", status_code=204)
def delete_entry(id: int):
    global _test_store
    _test_store = [e for e in _test_store if e.id != id]

# 4) Test-Seed

def seed_test_data():
    """Füllt _test_store beim App-Start mit ein paar Einträgen."""
    global _test_store
    _test_store.clear()
    _test_store.extend([
        TestEntry(id=1, title="Foo", description="Erster Test"),
        TestEntry(id=2, title="Bar", description="Zweiter Test"),
    ])