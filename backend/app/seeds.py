from sqlalchemy.orm import Session
from . import models

def seed_db(db: Session):
    contents = [
        models.Content(
            title="GitHub",
            description="Hier findest du mein GitHub Profil. Dort findest du auch den Code zu den Anwendungen auf meiner Seite.",
            body="Hier findest du mein GitHub Profil. Dort findest du auch den Code zu den Anwendungen auf meiner Seite.",
            image_url="/images/ScreenGH.png",
            links={"github": "https://github.com/MOTfromH"},
            has_view=True
        ),
        models.Content(
            title="Rollenspiel in PHP",
            description="Ein Rollenspiel, bei dem du als Mensch oder Ork gegeneinander antreten kannst. Bei der Wahl deiner Ausrüstung kannst du entweder auf einen festen Bonus setzen, oder du vertraust auf dein Glück.",
            body="Spiele als Mensch oder Ork gegeneinander. Ausrüstung: Festen Bonus oder Glück!",
            image_url="/images/orcKlein.png",
            links={"spielen": "/Rollenspiel_php/start.html"},
            has_view=True
        ),
        models.Content(
            title="Mein CV zum Download",
            description="Mein CV, Zeugnisse und Zertifikate findest du hier zum Download.",
            body="Mein CV, Zeugnisse und Zertifikate findest du hier zum Download. Der Downloadbereich ist passwortgeschützt.",
            image_url="/images/CVthumb.png",
            links={"download": "#exampleModal"},
            has_view=True
        ),
        models.Content(
            title="Kniffel API - JAVA & Spring Boot",
            description="Im Laufe der Zeit wird hier eine Kniffel-API entstehen. Verfolge das Voranschreiten des Projektes gerne auf GitHub.",
            body="Kniffel-API mit Java/Spring Boot. Projekt auf GitHub verfolgen.",
            image_url="/images/KniffelThumb.png",
            links={"github": "https://github.com/MOTfromH/springboot_workshop_kniffelAPI/tree/master"},
            has_view=True
        ),
        models.Content(
            title="Meine Homepage",
            description="Der Code zu meiner Homepage findet ihr auch bei GitHub. Er wird Stück für Stück weiter modulariesiert. Eine URL Router Class ist auch geplant.",
            body="Der Code zur Homepage ist auf GitHub – Modularisierung ongoing.",
            image_url="/images/HpSH.png",
            links={"github": "https://github.com/MOTfromH/motfromh"},
            has_view=True
        ),
        models.Content(
            title="Dynamisch erstellter Blog mit PHP",
            description="Projekt aus dem Fachunterricht. Verfolge das Projekt gerne mit auf GitHub, bis es fertig ist.",
            body="Dynamischer Blog in PHP. Entwicklung läuft – GitHub-Link im Button.",
            image_url="/images/blogPrev.PNG",
            links={"github": "https://github.com/MOTfromH/blog"},
            has_view=True
        ),
        models.Content(
            title="Sprite Animation mit JS",
            description="Animationen des Chars, verschiedene Gegnertypen mit unterschiedlichen Bewegungsmustern und ein Parallax Background kannst du hier entdecken.",
            body="Sprite Animation: Verschiedene Gegner, Parallax Background. Teste es selbst!",
            image_url="/images/spritePreview4.png",
            links={"starten": "/sprite/hallosprite.html"},
            has_view=True
        ),
    ]

    db.add_all(contents)
    db.commit()
