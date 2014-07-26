"""
Django settings for suggestion project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from .email_info import * 
# EMAIL_USE_TLS=EMAIL_USE_TLS
# EMAIL_HOST=EMAIL_HOST
# EMAIL_HOST_USER=EMAIL_HOST_USER
# EMAIL_HOST_PASSWORD=EMAIL_HOST_PASSWORD
# EMAIL_PORT = EMAIL_PORT

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'stevensanborn@gmail.com'
EMAIL_HOST_PASSWORD = 'Y@rdick3y2'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fx#)@+ap)8@nk3wuna1zxs)g0&ex!4*lc&edk2)r!98=f8q3m#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'signup',
    'box'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'suggestion.urls'

WSGI_APPLICATION = 'suggestion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'suggestion',                      
        'USER': 'stevensanborn',
        'PASSWORD': 'yeahdickey',
        'HOST': ''
    }
  #{'default': dj_database_url.config(default='postgres://stevensanborn:yeahdickey@localhost:5432/suggestion')}
}

DATABASES['default'] =  dj_database_url.config(default='postgresql://stevensanborn:yeahdickey@localhost:5432/suggestion')


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# TEMPLATES

TEMPLATE_DIRS = (os.path.join(PROJECT_PATH,"static","templates"))

if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT=(os.path.join(PROJECT_PATH,"static","static-only"))
    MEDIA_ROOT=(os.path.join(PROJECT_PATH,"static","media"))
    STATICFILES_DIRS = (
        (os.path.join(PROJECT_PATH,"static","static")),
    )


REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

