import os
from pathlib import Path
from google.cloud import storage
from google.oauth2.service_account import Credentials
from mongoengine import connect


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-n@3i10aug6x%oxlp=^^vu*&_+gdldc*w+a!*_zvnwq9j+j9!$7'

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'UploadImages',
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

ROOT_URLCONF = 'Guarented.urls'

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

WSGI_APPLICATION = 'Guarented.wsgi.application'

connect(db='Guarented', host='localhost', port=27017)

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

GOOGLE_CLOUD_STORAGE_BUCKET = "guarentedimages"
GOOGLE_CLOUD_STORAGE_ACCESS_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXX"
GOOGLE_CLOUD_STORAGE_SECRET_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXX"

key_path = os.path.join(BASE_DIR, 'creds.json')

credentials = Credentials.from_service_account_file(key_path)
storage_client = storage.Client(project=credentials.project_id, credentials=credentials)
bucket = storage_client.get_bucket(GOOGLE_CLOUD_STORAGE_BUCKET)