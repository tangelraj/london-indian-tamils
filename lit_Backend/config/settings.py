import os
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv


# ==========================================
# BASE DIRECTORY
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

FRONTEND_DIR = BASE_DIR.parent / "lit_frontend"

load_dotenv(BASE_DIR / ".env")


# ==========================================
# SECURITY SETTINGS
# ==========================================

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = os.environ.get(
    "DEBUG",
    "False"
).lower() == "true"


# ==========================================
# ALLOWED HOSTS
# ==========================================

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get(
        "ALLOWED_HOSTS",
        "127.0.0.1,localhost"
    ).split(",")
    if host.strip()
]


# Automatically add Render hostname

RENDER_EXTERNAL_HOSTNAME = os.environ.get(
    "RENDER_EXTERNAL_HOSTNAME"
)

if RENDER_EXTERNAL_HOSTNAME:

    if RENDER_EXTERNAL_HOSTNAME not in ALLOWED_HOSTS:

        ALLOWED_HOSTS.append(
            RENDER_EXTERNAL_HOSTNAME
        )


# ==========================================
# CSRF TRUSTED ORIGINS
# ==========================================

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get(
        "CSRF_TRUSTED_ORIGINS",
        ""
    ).split(",")
    if origin.strip()
]

if RENDER_EXTERNAL_HOSTNAME:

    render_origin = f"https://{RENDER_EXTERNAL_HOSTNAME}"

    if render_origin not in CSRF_TRUSTED_ORIGINS:

        CSRF_TRUSTED_ORIGINS.append(
            render_origin
        )


# ==========================================
# INSTALLED APPLICATIONS
# ==========================================

INSTALLED_APPS = [

    "django.contrib.admin",

    "django.contrib.auth",

    "django.contrib.contenttypes",

    "django.contrib.sessions",

    "django.contrib.messages",

    "django.contrib.staticfiles",

    # Website Application

    "website",
]


# ==========================================
# MIDDLEWARE
# ==========================================

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ==========================================
# URL CONFIGURATION
# ==========================================

ROOT_URLCONF = "config.urls"


# ==========================================
# FRONTEND HTML TEMPLATES
# ==========================================

TEMPLATES = [

    {
        "BACKEND": (
            "django.template.backends.django.DjangoTemplates"
        ),

        "DIRS": [

            FRONTEND_DIR / "templates",

        ],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

            ],

        },

    },

]


# ==========================================
# WSGI APPLICATION
# ==========================================

WSGI_APPLICATION = "config.wsgi.application"


# ==========================================
# DATABASE CONFIGURATION
# Local Development: SQLite
# Production: PostgreSQL when DATABASE_URL is set
# ==========================================

DATABASES = {

    "default": dj_database_url.config(

        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",

        conn_max_age=600,

        conn_health_checks=True,

    )

}


# ==========================================
# PASSWORD VALIDATION
# ==========================================

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },

    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },

    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },

    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },

]


# ==========================================
# LANGUAGE AND TIMEZONE
# ==========================================

LANGUAGE_CODE = "en-gb"

TIME_ZONE = "Europe/London"

USE_I18N = True

USE_TZ = True


# ==========================================
# STATIC FILES
# CSS, JAVASCRIPT AND STATIC IMAGES
# ==========================================

STATIC_URL = "/static/"

STATICFILES_DIRS = [

    FRONTEND_DIR / "static",

]

STATIC_ROOT = BASE_DIR / "staticfiles"


# ==========================================
# MEDIA FILES
# LOCAL AND RENDER CONFIGURATION
# ==========================================

if DEBUG:

    # Local development

    MEDIA_URL = "/media/"

    MEDIA_ROOT = BASE_DIR / "media"

else:

    # Render deployment
    # Serve existing public images copied to static

    MEDIA_URL = "/static/website_media/"

    MEDIA_ROOT = (
        FRONTEND_DIR / "static" / "website_media"
    )


# ==========================================
# FILE STORAGE CONFIGURATION
# ==========================================

STORAGES = {

    "default": {

        "BACKEND": (
            "django.core.files.storage.FileSystemStorage"
        ),

    },

    "staticfiles": {

        "BACKEND": (

            "django.contrib.staticfiles.storage.StaticFilesStorage"

            if DEBUG

            else

            "whitenoise.storage.CompressedManifestStaticFilesStorage"

        ),

    },

}


# Keep original static filenames available
# Required for existing public media image URLs

WHITENOISE_KEEP_ONLY_HASHED_FILES = False


# ==========================================
# DEFAULT PRIMARY KEY
# ==========================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ==========================================
# EMAIL CONFIGURATION
# ==========================================

MAILERS = {

    "default": {

        "BACKEND": (
            "django.core.mail.backends.console.EmailBackend"
        ),

    },

}


# ==========================================
# PRODUCTION SECURITY
# ==========================================

SECURE_PROXY_SSL_HEADER = (

    "HTTP_X_FORWARDED_PROTO",

    "https"

)

SECURE_SSL_REDIRECT = not DEBUG

SESSION_COOKIE_SECURE = not DEBUG

CSRF_COOKIE_SECURE = not DEBUG

SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = "DENY"

SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"