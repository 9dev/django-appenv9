
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Add our Django app to path
sys.path.insert(0, os.path.dirname(BASE_DIR))

SECRET_KEY = '!@rf6@w&uz5b#8hk_^@b2fr^t163el(@0uf!xahiuc@k13hfru'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

	'debug_toolbar',
	'||APP_NAME||',
	'main',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'demo.urls'
WSGI_APPLICATION = 'demo.wsgi.application'

SILENCED_SYSTEM_CHECKS = (
    '1_6.W001',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

from django.conf import settings

# Add our app's templates to TEMPLATE_DIRS
TEMPLATE_DIRS = settings.TEMPLATE_DIRS + (       
    os.path.join(os.path.dirname(BASE_DIR), '||APP_NAME||/templates'),
)

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')

DEBUG_TOOLBAR_PATCH_SETTINGS = False

