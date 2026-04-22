from .base import *

DEBUG = False

ALLOWED_HOSTS = ['tudominio.com']

# Ejemplo con PostgreSQL (puedes cambiarlo luego)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_db',
        'USER': 'usuario',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Seguridad extra
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True