"""
Django settings for Livarava-Neuroner project.
"""

import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


ALLOWED_HOSTS = ['127.0.0.1']
SITE_ID = 1


sys.path.append(os.path.join(BASE_DIR, 'apps'), )


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'djangobower',
    'crispy_forms',

    "geoposition",
    "geo",
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'web', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'web', 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder', # BOWER_COMPONENTS
)

# BOWER_COMPONENTS
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'static')
BOWER_INSTALLED_APPS = (
    'jquery#2.*',
    'bootstrap#4.0.0-alpha.2',
    'lodash#4.*',
    'font-awesome#4.*',
)
# END BOWER_COMPONENTS








GEOPOSITION_MAP_WIDGET_HEIGHT = 500
 


# CRISPY FORM TAGs SETTINGS
CRISPY_TEMPLATE_PACK = 'bootstrap3'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'logs', 'email')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'django_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'django.log'),
            'formatter': 'verbose'
        },
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'debug.log'),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['django_file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'debug': {
            'handlers': ['debug_file'],
            'level': 'DEBUG',
        },
    }
}