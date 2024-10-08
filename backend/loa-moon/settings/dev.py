import os
from django.core.management.utils import get_random_secret_key
from corsheaders.defaults import default_headers

from .base import *


print("\n\033[92mYOU'RE CONNECTED TO THE DEVELOPMENT SETTINGS.\033[0m\n")


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_random_secret_key()


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# CSRF settings, only for development
CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:5173"]


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}
