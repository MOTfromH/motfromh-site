# motfromh-site

## Einleitung

In diesem Projekt entsteht eine neue Version meiner Website, da die alte nicht mehr meinen aktuellen Fähigkeiten entspricht. Gleichzeitig nutze ich die Gelegenheit, um neue Technologien kennenzulernen und bestehende Skills weiter zu vertiefen.

## Was ist geplant?

- **API-First-Ansatz**  
  Trotz meiner bisherigen positiven Erfahrungen mit Ruby on Rails setze ich hier auf eine entkoppelte Architektur. Das ermöglicht es, Frontend und Backend jederzeit modular zu erweitern oder auszutauschen.
- **CI/CD-Pipelines**  
  Mein Ziel ist es, automatisierte Build- und Deployment-Pipelines (CI/CD) einzurichten und praxisnah zu erproben.
- **Containerisierung mit Docker**  
  Ich werde alle Services containerisieren und Best Practices für Images, Volumes und Netzwerke anwenden.

## Tech-Stack

- **Server-OS:** NixOS  
  Mit `nix-shell` / Flakes bekomme ich reproduzierbare Dev-Environments auf nur einem gehosteten Server, ohne Abhängigkeitskonflikte.
- **Backend:** Python 3.11 + FastAPI
  - Modularer Aufbau: Models, Schemas, Routes, CRUD-Services
  - Datenbankzugriff über SQLAlchemy
  - Automatischer Tabellen-Erstellung beim App-Start
- **Datenbank:** PostgreSQL 15 (Docker-Container)
- **Frontend:** Vue.js (separater Service auf Port 5173)
- **DevOps:**
  - Docker Compose für `db`, `api`, `web`
  - CI/CD mit GitHub Actions (geplant)
  - Environment-Variablen via `.env`

## Aktueller Stand (Stand: 2025-05-16)

### 🚀 Umgesetzte Features (Backend)

**Basis:** `/api/v1`

- `GET    /content/` → alle Inhalte abrufen
- `GET    /content/new/` → neueste Inhalte
- `GET    /content/featured/` → empfohlene Inhalte
- `GET    /content/{id}/` → Einzelansicht
- `POST   /content/` → neuen Inhalt erstellen
- `PUT    /content/{id}/` → bestehenden Inhalt aktualisieren
- `DELETE /content/{id}/` → Inhalt löschen

### 🐳 Docker & Infrastruktur

- **API** läuft im Docker-Container (`python:3.11.9-slim`)
- **DB** als separater Container mit Volume `postgres_data`
- CORS für `localhost:5173` aktiviert

### 📋 To-Do

- [ ] Dockerfile finalisieren (Multi-Stage Build)
  - [x] Dockerfile für das Backend
  - [ ] Dockerfile für das Frontend
- [ ] Frontend-Service mit Vue.js implementieren
  - [x] Projekt initialieseiren
  - [x] Erster data-fetch
  - [ ] Card-Component bauen
  - [ ] Navbar, Heder und Footer-Components erstellen
- [ ] Admin-Bereich mit Login/Rollensteuerung
- [ ] Automated Tests mit `pytest` schreiben
- [x] Seed-Skript bzw. Migrationstool für Testdaten
- [ ] CI/CD-Workflows (Build → Test → Deploy) konfigurieren
- [ ] Rollout in Produktionsumgebung (z. B. Docker Swarm / Kubernetes)

---

**Tech-Stack auf einen Blick:**  
| Komponente | Technologie | Status |
|-------------------|---------------------|----------------|
| Betriebssystem | NixOS | in Betrieb |
| Backend | FastAPI (Python) | funktional |
| Datenbank | PostgreSQL 15 | via Docker |
| Frontend | Vue.js | in Arbeit |
| Containerization | Docker, Docker Compose | eingerichtet |
| CI/CD | GitHub Actions | geplant |
