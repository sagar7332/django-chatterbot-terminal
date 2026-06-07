"""Minimal Django settings for the terminal ChatterBot client."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-terminal-chatbot-development-key"
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = ["django.contrib.contenttypes", "django.contrib.auth", "chatbot"]
MIDDLEWARE = []
ROOT_URLCONF = "chatbot_project.urls"
TEMPLATES = []
WSGI_APPLICATION = "chatbot_project.wsgi.application"
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "django_db.sqlite3"}}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
