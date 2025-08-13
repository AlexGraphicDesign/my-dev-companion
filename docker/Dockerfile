FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1 \
    PIP_NO_CACHE_DIR=1

COPY app/ .

RUN pip install --no-cache-dir -e .

CMD ["tail", "-f", "/dev/null"]
