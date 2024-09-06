import os
from django.core.management.utils import get_random_secret_key

from .base import *


print("\n\033[92mYOU'RE CONNECTED TO THE DEVELOPMENT SETTINGS.\033[0m\n")


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_random_secret_key()


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# CORS settings, only for development
staticfiles_index = INSTALLED_APPS.index("django.contrib.staticfiles")
INSTALLED_APPS.insert(staticfiles_index + 1, "corsheaders")
commonmiddleware_index = MIDDLEWARE.index("django.middleware.common.CommonMiddleware")
MIDDLEWARE.insert(commonmiddleware_index, "corsheaders.middleware.CorsMiddleware")

CORS_ALLOWED_ORIGINS = ["http://127.0.0.1:5173"]
CORS_ALLOW_CREDENTIALS = True

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
