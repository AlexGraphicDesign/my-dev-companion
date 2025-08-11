FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

COPY ./src /app
