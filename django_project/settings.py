import os
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

ADMINS = (
    ('Guillermo','guillermo@bandtastic.me'),
)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'dev@bandtastic.me'
EMAIL_HOST_PASSWORD = 'exbFsMjq7fKmyTFRZR'
EMAIL_PORT = 587

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'database.sqlite',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


TIME_ZONE = 'America/Mexico_City'
LANGUAGE_CODE = 'es-mx'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'
MEDIA_ROOT = os.path.join(ROOT_PATH,'static/media/')
MEDIA_URL = os.path.join(ROOT_PATH,'static/')
COMPRESS_URL = STATIC_URL

STATICFILES_DIRS = (
    os.path.join(ROOT_PATH,'static'),
)

COMPRESS_ROOT = STATICFILES_DIRS[0]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder', 
)

SECRET_KEY = 'ye5kgt9aqr#k-c+fkbqw*jxnr=h5&li0l862@laza%j1sz3k()'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    ('shpaml.Loader',
        ('django.template.loaders.filesystem.Loader',)
    ),
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
   os.path.join(ROOT_PATH, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'main.global_context_processors.basics',
)


MIDDLEWARE_CLASSES = (
    'main.middleware.Generic',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'django.contrib.auth.backends.ModelBackend',
    )

LOGIN_URL          = '/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/'

ROOT_URLCONF = 'django_project.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    
    'django_extensions',
    'annoying',
    'south',
    'compressor',
    'social_auth',
    
    'main',
)

COMPRESS_PRECOMPILERS = (
    ('text/x-sass','/home/grillermo/.rvm/gems/ree-1.8.7-2011.03/bin/sass {infile} {outfile} --style compressed'),
    ('text/x-scss','/home/grillermo/.rvm/gems/ree-1.8.7-2011.03/bin/sass --scss {infile} {outfile}'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
