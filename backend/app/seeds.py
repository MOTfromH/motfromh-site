from sqlalchemy.orm import Session
from . import models
from datetime import datetime

def seed_db(db: Session):
    contents = [
        models.Content(
            title="Hello World",
            description="Ein einfacher Testeintrag",
            body="Lorem ipsum dolor sit amet.",
            image_url="/static/test1.jpg",
            links={"github": "https://github.com/yourorg/hello-world"},
            has_view=True
        ),
        models.Content(
            title="Projekt Eins",
            description="Beschreibung zu Projekt Eins",
            body="Dies ist der Body von Projekt Eins.",
            image_url="/static/test2.jpg",
            links={"github": "https://github.com/yourorg/projekt-eins"},
            has_view=True
        ),
        models.Content(
            title="Projekt Zwei",
            description="Kurzbeschreibung von Projekt Zwei",
            body="Detailierter Text zu Projekt Zwei.",
            image_url="/static/test3.jpg",
            links={"github": "https://github.com/yourorg/projekt-zwei"},
            has_view=True
        ),
        models.Content(
            title="Mini-App",
            description="Eine kleine Beispiel-App",
            body="Hier steht der längere Text zu Mini-App.",
            image_url="/static/test4.jpg",
            links={"github": "https://github.com/yourorg/mini-app"},
            has_view=True
        ),
        models.Content(
            title="Starter Pack",
            description="Basis-Template zum Ausprobieren",
            body="Erklärungen und Hinweise zum Starter Pack.",
            image_url="/static/test5.jpg",
            links={"github": "https://github.com/yourorg/starter-pack"},
            has_view=True
        ),
        models.Content(
            title="Demo Card",
            description="Reine Platzhalter-Eintragung",
            body="Kurzbeschreibung für die Demo Card.",
            image_url="/static/test6.jpg",
            links={"github": "https://github.com/yourorg/demo-card"},
            has_view=True
        ),
    ]

    db.add_all(contents)
    db.commit()