import os
import dj_database_url
from pathlib import Path

# Construir rutas dentro del proyecto (BASE_DIR apunta donde está manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURIDAD: Mantén la clave secreta en secreto en producción
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-debug-key-123')

# DEBUG: En desarrollo True, en producción debe ser False
DEBUG = True

# Permitir todos los hosts en desarrollo para que el proxy pueda conectar
ALLOWED_HOSTS = ['*']

# Permite que Django confíe en los nombres que le envía el Proxy
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Definición de aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    
    # --- CONFIGURACIÓN SSO V2 ---
    # Este middleware detecta al usuario que el oauth2-proxy inyecta en la cabecera
    'core.middleware.XForwardedUserMiddleware',
    # 'django.contrib.auth.middleware.RemoteUserMiddleware',
    
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de los Backends de Autenticación
AUTHENTICATION_BACKENDS = [
    # 1. Permite autenticar basándose en la cabecera del proxy
    # 'django.contrib.auth.backends.RemoteUserBackend',
    'core.backends.KeycloakRemoteUserBackend',  # ← reemplaza RemoteUserBackend
    # 2. Mantiene el login tradicional (útil para el admin de Django)
    'django.contrib.auth.backends.ModelBackend',
]

# Cabecera que enviará el oauth2-proxy (X-Forwarded-User)
# Django antepone 'HTTP_' y convierte guiones en guiones bajos
# AUTHENTICATION_HEADER = 'HTTP_X_FORWARDED_USER'

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Base de Datos Unificada (MySQL)
# Lee la URL de la variable de entorno configurada en el docker-compose
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
    )
}

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Configuración de idioma y zona horaria
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Tipo de campo por defecto para llaves primarias
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'