#!/bin/sh

echo "Esperando a MySQL..."

# Intentamos conectar al puerto 3306 del servicio 'mysql_server'
while ! nc -z mysql_server 3306; do
  echo "Esperando a MySQL en el host 'mysql_server'..."
  sleep 0.1
done

echo "MySQL está listo...... !!!!!"

# Ejecutar migraciones (opcional, pero recomendado en desarrollo)
python manage.py migrate

# Arrancar el servidor de desarrollo
python manage.py runserver 0.0.0.0:8000