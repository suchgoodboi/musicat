# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from decouple import config, Csv
from dj_database_url import parse as db_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-zx09@9c!=f27t&mzq#%@c$3_n1!1nu#)a(7jua9_1m@=d=&wk'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = config('DEBUG', default=False, cast=bool)
DEBUG = True

INTERNAL_IPS = config('INTERNAL_IPS', default='', cast=Csv())

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
)

THIRD_PARTS_APPS = (
    'compressor',
    'corsheaders',
    'crispy_forms',
    'easy_thumbnails',
    'opbeat.contrib.django',
    'password_reset',
    'rest_framework',
)

PROJECT_APPS = (
	'songs',
	'users',
	'api',
)

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTS_APPS

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

PROJECT_TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, '../templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', PROJECT_TEMPLATE_LOADERS),
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


ROOT_URLCONF = 'musicat.urls'

WSGI_APPLICATION = 'musicat.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

conn_max_age = config('DB_CONN_MAX_AGE', default=0, cast=int)
DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'musicat_db',
        'USER': 'djangouser',
        'PASSWORD': 'djangouser',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-EN'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

# Setting static folder for site-wide files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../static'),
)

# static root folder, where static files will be collected to
STATIC_ROOT = os.path.join(BASE_DIR, '../../static_root')


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder"
]

COMPRESS_OFFLINE = True

# Setting media configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../../media')

# Setting easy_thumbnails
THUMBNAIL_ALIASES = {
    '': {
        'song_thumb': {'size': (350, 350), 'crop': True, 'upscale': True},
        'song_poster': {'size': (550, 550), 'crop': True, 'upscale': True},
    }
}

THUMBNAIL_BASEDIR = 'group_thumbs'

LOGIN_URL = 'users:login'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

AUTH_USER_MODEL = 'users.OwnerProfile'


# Authentication
#SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'users:confirm_information'

# Number of days used to consider a register staled
DAYS_TO_STALE_REGISTER = config('DAYS_TO_STALE_REGISTER', default=90, cast=int)

OPBEAT = {
    'ORGANIZATION_ID': config('OPBEAT_ORGANIZATION_ID', default=''),
    'APP_ID': config('OPBEAT_APP_ID', default=''),
    'SECRET_TOKEN': config('OPBEAT_SECRET_TOKEN', default=''),
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}
