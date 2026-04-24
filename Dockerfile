# Usamos una imagen base oficial de Python 3.10
FROM python:3.10-slim

# Evita que Python genere archivos .pyc y permite ver logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo dentro del contenedor
WORKDIR /code

# Instalamos dependencias del sistema necesarias para mysqlclient
# y para que la base de datos espere a estar lista (netcat)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Instalamos las dependencias de Python
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# 2. Copiamos el código de Django
# Esto mete el contenido de TU carpeta core local en /code del contenedor
COPY ./core /code/

# 3. Copiamos el script de arranque que está en la raíz local
COPY entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh

ENTRYPOINT ["/code/entrypoint.sh"]