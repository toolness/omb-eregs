"""
Django settings for omb_eregs project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

import dj_database_url
from cfenv import AppEnv
from django.utils.crypto import get_random_string

env = AppEnv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get_credential('DJANGO_SECRET_KEY', get_random_string(50))

DEBUG = os.environ.get('DEBUG', 'FALSE').upper() == 'TRUE'

ALLOWED_HOSTS = env.uris


# Application definition

INSTALLED_APPS = (
    'reqs.apps.ReqsConfig',
    'taggit',
    'django.contrib.contenttypes',
    # must be after taggit and contenttypes, but before auth
    'ereqs_admin.apps.EreqsAdminConfig',
    'corsheaders',
    'dal',
    'dal_select2',
    'django_filters',
    'rest_framework',
    'reversion',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
if DEBUG:
    INSTALLED_APPS += ('debug_toolbar', )

MIDDLEWARE = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)
if DEBUG:
    MIDDLEWARE = ('debug_toolbar.middleware.DebugToolbarMiddleware',) + \
                 MIDDLEWARE

# Allow most URLs to be used by any service; do not allow the admin to be
# accessed this way
CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/(?!admin).*$'

# Request the browser not allow the CSRF cookie to be used in JS (not: this
# means we can't have AJAX forms)
CSRF_COOKIE_HTTPONLY = True
# Request browsers block XSS attacks when they can
SECURE_BROWSER_XSS_FILTER = True
# Request browsers not guess at mimetypes
SECURE_CONTENT_TYPE_NOSNIFF = True
# Request cookies only be sent over SSL
USING_SSL = env.get_credential('USING_SSL', 'TRUE').upper() == 'TRUE'
SESSION_COOKIE_SECURE = USING_SSL
CSRF_COOKIE_SECURE = USING_SSL

# For the time being, tell downstream (notably CloudFront) to avoid caching
# content rather than guessing.
CACHE_MIDDLEWARE_SECONDS = 0

ROOT_URLCONF = 'omb_eregs.urls'

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

WSGI_APPLICATION = 'omb_eregs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'))
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.{0}'.format(validator)}
    for validator in (
        'UserAttributeSimilarityValidator', 'MinimumLengthValidator',
        'CommonPasswordValidator', 'NumericPasswordValidator')
]

MAX_URL = os.environ.get('MAX_URL')

if MAX_URL:
    INSTALLED_APPS += ('django_cas_ng',)
    AUTHENTICATION_BACKENDS = ['ereqs_admin.max_backend.MAXBackend']
    CAS_SERVER_URL = MAX_URL
    CAS_REDIRECT_URL = '/admin/'
    # The following attributes are ignored in our implementation, including
    # as documentation
    CAS_CREATE_USER = False
    CAS_USERNAME_ATTRIBUTE = 'Email-Address'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get('TMPDIR', '.') + '/static/'

TAGGIT_CASE_INSENSITIVE = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(name)-20s %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    }
}

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 25,
}

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'omb_eregs.utils.show_toolbar',
}
