# motfromh-site

## Einleitung

In diesem Projekt entsteht eine neue Version meiner Website, da die alte nicht mehr meinen aktuellen Fähigkeiten entspricht. Gleichzeitig nutze ich die Gelegenheit, um neue Technologien kennenzulernen und bestehende Skills weiter zu vertiefen.

## Was ist geplant?

- **API-First-Ansatz**  
  Trotz meiner bisherigen positiven Erfahrungen mit Ruby on Rails setze ich hier auf eine entkoppelte Architektur. Das ermöglicht es, Frontend und Backend jederzeit modular zu erweitern oder auszutauschen.
- **CI/CD-Pipelines**  
  Ziel ist der Aufbau automatisierter Build- und Deployment-Pipelines (CI/CD) mit GitHub Actions.
- **Containerisierung mit Docker**  
  Alle Services laufen containerisiert. Best Practices für Images, Volumes und Netzwerke werden berücksichtigt.
- **Moderne UI-Komponenten mit Nuxt 3**  
  Der Fokus liegt auf einem dynamischen und reaktiven Frontend, das klar strukturiert und leicht erweiterbar ist.

## Tech-Stack

- **Server-OS:** NixOS  
  Mit `nix-shell` / Flakes lassen sich reproduzierbare Entwicklungsumgebungen schaffen – ohne Konflikte.
- **Backend:** Python 3.11 + FastAPI
  - Modularer Aufbau mit `models`, `schemas`, `routes`, `crud`, `database`, `seeds`
  - SQLAlchemy für ORM + Startup-Seeding
  - CORS für lokale Entwicklung (Port 5173)
- **Datenbank:** PostgreSQL 15 (Docker-Container)
- **Frontend:** Nuxt 3 (Vue 3 + TypeScript)
  - Seiten: `pages/index.vue`, `pages/content/[id].vue`
  - Komponenten: `CardContent`, `Navbar`, `Banner`, `Footer`
  - Features:
    - Hover-Animation & Card-Schatten
    - Automatische Erkennung von Textüberlauf
    - Dynamische „Mehr anzeigen“-Funktion mit Fade-Out-Effekt
    - Bootstrap 5 Styling + eigene CSS-Overrides
- **DevOps & Infrastruktur:**
  - Docker Compose (`db`, `api`, `web`)
  - Multi-Stage-Build für API
  - CI/CD via GitHub Actions (in Planung)
  - Konfiguration über `.env`-Dateien

## Aktueller Stand (Stand: 2025-05-22)

### ✅ Backend: `/api/v1/content/`

- `GET    /content/` → alle Inhalte
- `GET    /content/new/` → neueste 3 Inhalte
- `GET    /content/featured/` → empfohlene Inhalte
- `GET    /content/{id}/` → Detailansicht
- `POST   /content/` → neuen Inhalt anlegen
- `PUT    /content/{id}/` → Inhalt aktualisieren
- `DELETE /content/{id}/` → Inhalt löschen

### ✅ Frontend (Nuxt 3)

- Card-Komponente mit:
  - Einheitlicher Bild- & Textfläche
  - Hover-Zoom & Schatten
  - "Mehr anzeigen"-Toggle mit Fade-Out-Gradiant
- Global Layout via `layouts/default.vue`
- Automatischer API-Fetch mit `useFetch`
- Bootstrap 5 + eigenes `main.css`
- Bilder aus `assets/images/`, lazy loading aktiv

### 🐳 Docker & Infrastruktur

- API im `python:3.11-slim` Container
- DB mit Volume `postgres_data`
- Frontend im Nuxt Container (`node:18-alpine`)
- Lokale Ports: API (`8001`), Web (`5173`)
- Dev-CORS aktiviert

## 📋 To-Do

- [x] Card-Komponente mit dynamischem Text & Fade-Out
- [x] Layoutstruktur (Navbar, Banner, Footer)
- [x] Seed-Skript bzw. Testdaten
- [ ] Authentifizierung & Admin-Bereich (Login, Rollen)
- [ ] Integrationstests mit `pytest`, später TDD für Features
- [ ] Dockerfile für Nuxt-Frontend abschließen
- [ ] CI/CD-Pipeline (GitHub Actions) konfigurieren
- [ ] Deployment auf Produktivumgebung (Docker Swarm o. Ä.)

---

## 🧠 Teststrategie (ab v1 Live)

Zukünftige Features werden **testgetrieben (TDD)** entwickelt:

- Frontend: Vitest + Testing Library
- Backend: pytest + httpx
- Fokus auf Integration, Regression und UX-Stabilität

---

**Tech-Stack auf einen Blick:**

| Komponente     | Technologie           | Status        |
| -------------- | --------------------- | ------------- |
| Betriebssystem | NixOS                 | aktiv         |
| Backend        | FastAPI (Python 3.11) | einsatzbereit |
| Datenbank      | PostgreSQL 15         | via Docker    |
| Frontend       | Nuxt 3 (Vue 3 + TS)   | in Arbeit     |
| Styling        | Bootstrap 5 + CSS     | aktiv         |
| Container      | Docker + Compose      | produktiv     |
| CI/CD          | GitHub Actions        | in Planung    |
| Testing        | pytest / vitest       | vorbereitet   |

---

**Letzter Stand:** `v1 (Preview)` läuft lokal. Deployment & Testinfrastruktur folgen als nächstes. 🚀
