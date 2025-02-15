"""
Django settings for gotilo project.

Generated by 'django-admin startproject' using Django 4.2.18.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-or!*g**fs@uky=kjb_egk*m^kxn)44d@#n$mysk@$mfcdq#^#7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ["*",'https://web-production-a183.up.railway.app',".vercel.app","10.0.2.2","127.0.0.1","localhost",".now.sh"]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
    "http://10.0.2.2:8000",
    "http://127.0.0.1:3001",
    "http://localhost:8080",
    "http://localhost:5173",
    
]
CSRF_TRUSTED_ORIGINS = [
    'https://web-production-a183.up.railway.app',
    # Add any other domains you need
]

# Also make sure your ALLOWED_HOSTS includes your domain
ALLOWED_HOSTS = [
    'web-production-a183.up.railway.app',
    'localhost',
    '127.0.0.1',
    # Add any other domains you need
]

# If you're using CORS headers, you might also want to configure:
CORS_ALLOWED_ORIGINS = [
    'https://web-production-a183.up.railway.app',
    # Add any other domains you need
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jetship',
    'import_export', 
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'gotilo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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

WSGI_APPLICATION = 'gotilo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles'),
]
# Add this if not already present
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Default primary key field types

CLOUDFLARE_R2_BUCKET=config("CLOUDFLARE_R2_BUCKET",default=None)
CLOUDFLARE_R2_BUCKET_ENDPOINT=config("CLOUDFLARE_R2_BUCKET_ENDPOINT",default=None)
CLOUDFLARE_R2_ACCESS_KEY=config("CLOUDFLARE_R2_ACCESS_KEY",default=None)
CLOUDFLARE_R2_SECRET_KEY=config("CLOUDFLARE_R2_SECRET_KEY",default=None)

if not CLOUDFLARE_R2_BUCKET or not CLOUDFLARE_R2_BUCKET_ENDPOINT:
    raise ValueError("Cloudflare R2 Bucket or Endpoint is missing!")


CLOUDFLARE_R2_CONFIG_OPTIONS = {
    "bucket_name" : CLOUDFLARE_R2_BUCKET,
    "access_key" : CLOUDFLARE_R2_ACCESS_KEY,
    "secret_key" : CLOUDFLARE_R2_SECRET_KEY,
    "endpoint_url" : CLOUDFLARE_R2_BUCKET_ENDPOINT,
    "default_acl" : "public-read",
    "signature_version" : "s3v4",
}

STORAGES = {
        "default": {
            "BACKEND": "helpers.cloudflare.storage.mediaFileStorage",
            "OPTIONS": CLOUDFLARE_R2_CONFIG_OPTIONS,
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
            # Use local storage for static files even in production
        },
    }

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST_FRAMEWORK = {
#     'DEFAULT_RENDERER_CLASSES': (
#         'rest_framework.renderers.JSONRenderer',  # Force JSON response
#     ),
#     'DEFAULT_PARSER_CLASSES': (
#         'rest_framework.parsers.JSONParser',
#     ),
# }

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
}


# APPEND_SLASH=False