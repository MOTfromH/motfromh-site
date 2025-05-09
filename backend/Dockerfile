# 1️. Build stage: Python base image and dependencies
FROM python:3.11.9-slim AS builder
# Maybe use SHA image for prod builds?

# Install build dependencies
RUN apt-get update \
    && apt-get install -y build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python packages (uses psycopg2-binary)
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# 2️. Final stage: minimal runtime image
FROM python:3.11.9-slim

WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /root/.local /root/.local
ENV PATH="/root/.local/bin:$PATH"

# Copy application code
COPY app/ .

# Entrypoint
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]