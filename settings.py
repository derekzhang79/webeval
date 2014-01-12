import os
import socket

import djcelery
djcelery.setup_loader()

import dotenv
dotenv.read_dotenv()

import config.databases

from config.apikeys.akismet import *
from config.apikeys.facebook import *
from config.apikeys.google import *
from config.apikeys.reCaptcha import *
from config.apikeys.twitter import *
from config.filesystem import *

ENVIRONMENT = env('DJANGO_ENV')
DEBUG = ENVIRONMENT != 'production'
TEMPLATE_DEBUG = DEBUG
CELERY_ALWAYS_EAGER = True
DATABASES = config.databases.SETTINGS[ENVIRONMENT]
HOST_URL  = env('HOST_URL')
MEDIA_HOST_URL = "%s:8000/static" % HOST_URL

PROJECT_DIRECTORY = os.path.dirname(__file__)

ADMINS = (
    ('Teodor Pripoae', 'teodor.pripoae@gmail.com')
)

MANAGERS = ADMINS

TIME_ZONE = 'Europe/Bucharest'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

# Ip's allowed to connect to API
INTERNAL_IPS = env('INTERNAL_IPS').split(',')

MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = 'public'
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIRECTORY),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'static_precompiler.finders.StaticPrecompilerFinder'
)

SECRET_KEY = env('SECRET_KEY')

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'app.middleware.keep_me_logged_in.KeepLoggedInMiddleware'
    #'django.middleware.cache.FetchFromCacheMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'lib.auth_backend.FacebookBackend',
    'lib.auth_backend.GoogleBackend',
    'lib.auth_backend.TwitterBackend',
)


ROOT_URLCONF = 'config.routes'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIRECTORY, 'app', 'views'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
   # "socialauth.context_processors.facebook_api_key",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",

    'django.core.context_processors.media',
    'django.core.context_processors.static',
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.comments',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.markup',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_extensions',
    'djcelery',
    'south',
    'captcha',
    'django_nose',
    'annoying',
    'static_precompiler',
    'app',
)

NOSE_ARGS = ['-v', '--with-snot', '-s']
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'
KEEP_LOGGED_KEY      = 'keep_me_logged' # session key
KEEP_LOGGED_DURATION = 14               # in days

CELERY_RESULT_BACKEND = "database"
# os.environ["CELERY_LOADER"] = "django"
BROKER_URL=env("BROKER_URL")
#CACHE_BACKEND = ''
#CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

SCSS_EXECUTABLE="sass"
STATIC_PRECOMPILER_OUTPUT_DIR="compiled"

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
