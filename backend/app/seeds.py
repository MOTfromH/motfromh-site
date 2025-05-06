from sqlalchemy.orm import Session
from . import models

def seed_db(db: Session):
    example = models.Content(
        title="Hello World",
        description="Ein Testprojekt",
        body="Lorem ipsum...",
        image_url="/static/test.jpg",
        links={"github": "https://github.com/..."},
        has_view=True
    )
    db.add(example)
    db.commit()
