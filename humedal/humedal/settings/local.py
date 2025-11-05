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

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

JAZZMIN_SETTINGS = {
    "site_title": "Administración Humedal UCN",
    "site_header": "Administración Humedal",
    "welcome_sign": "Bienvenida al Sistema UCN",
    "site_brand": "UCN Humedal",
    "site_logo": "img/logo_ucn.png",
    "custom_css": "css/admin_custom.css",
    "custom_js": None,
     ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "socios"},
        {"app": "inicio"},
    ],
    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],



}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    "dark_mode_theme": "darkly",
}