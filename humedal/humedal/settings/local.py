from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_humedal',
        'USER': 'user_humedal',
        'PASSWORD': 'culebron123',
        'HOST': 'localhost',
        'PORT':'5432'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / "static"]
# 🔹 Agrega esta línea:
STATIC_ROOT = BASE_DIR / "staticfiles"

JAZZMIN_SETTINGS = {
    "site_title": "Administración Humedal UCN",
    "site_header": "Administración Humedal",
    "welcome_sign": "Bienvenida al Sistema UCN",
    "site_brand": "UCN Humedal",
    "site_logo": "img/logo_ucn.png",
    "custom_css": "css/admin_custom.css",
    "custom_js": None,
}