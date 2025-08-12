FROM python:3.13-slim

WORKDIR /app

# Installer les dépendances système si besoin
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copier uniquement les fichiers nécessaires à l’installation
COPY pyproject.toml requirements.txt ./
COPY src/ ./src/

RUN pip install --no-cache-dir -e .
