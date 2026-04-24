-- 1. Crear las bases de datos
CREATE DATABASE IF NOT EXISTS keycloak;
CREATE DATABASE IF NOT EXISTS django_db;

-- 2. Crear usuario para Keycloak y darle permisos solo en su BD
CREATE USER IF NOT EXISTS 'kc_admin'@'%' IDENTIFIED BY 'pass_keycloak_987';
GRANT ALL PRIVILEGES ON keycloak.* TO 'kc_admin'@'%';

-- 3. Crear usuario para Django y darle permisos solo en su BD
CREATE USER IF NOT EXISTS 'django_admin'@'%' IDENTIFIED BY 'pass_django_654';
GRANT ALL PRIVILEGES ON django_db.* TO 'django_admin'@'%';

-- 4. Aplicar cambios
FLUSH PRIVILEGES;