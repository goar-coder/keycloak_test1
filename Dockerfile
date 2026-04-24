FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# Instalamos dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Instalamos requisitos
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# COPIAMOS TODO EL PROYECTO (Incluyendo manage.py si aparece por ahí)
COPY . /code/