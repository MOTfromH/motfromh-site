# 1️⃣ Build-Image mit Python + Abhängigkeiten
FROM python:3.11.9-slim AS builder

# Nur notwendig für das Kompilieren mancher Wheels
RUN apt-get update \
    && apt-get install -y build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Python-Pakete installieren (nutzt jetzt psycopg2-binary)
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# 2️⃣ Finales, minimales Runtime-Image
FROM python:3.11.9-slim

WORKDIR /app

# Nur das vom Builder installierte user–Verzeichnis übernehmen
COPY --from=builder /root/.local /root/.local
ENV PATH="/root/.local/bin:$PATH"

# Applikations-Code übernehmen
COPY app/ .

# Startbefehl
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
