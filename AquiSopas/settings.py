"""
Django settings for AquiSopas project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from oscar import OSCAR_MAIN_TEMPLATE_DIR
from oscar import get_core_apps
from oscar.defaults import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')czg)ebcc0s18&@*-*xdr64hq6%t4(yo=5b23kahbm0*kn+9)k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

COMPRESS_ENABLED = True

COMPRESS_OFFLINE = True

COMPRESS_CSS_FILTERS = ["compressor.filters.cssmin.CSSMinFilter"]

COMPRESS_JS_FILTERS = ["compressor.filters.jsmin.JSMinFilter"]

OSCAR_USE_LESS = False

ALLOWED_HOSTS = ['*']

OSCAR_SHOP_NAME = "Aqui Sopas"
OSCAR_DEFAULT_CURRENCY = "L "

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'widget_tweaks',
    'storages',
    'paybac',
    'anymail',
    'compressor'
]
INSTALLED_APPS = INSTALLED_APPS + get_core_apps(['shipping','checkout'])

OSCAR_ALLOW_ANON_CHECKOUT = True

OSCAR_REQUIRED_ADDRESS_FIELDS = ['first_name','line1','city','phone_number']


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATIC_ROOT = os.path.join(BASE_DIR,'staticos')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'template_statics'),
)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'AquiSopas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates'),
            OSCAR_MAIN_TEMPLATE_DIR
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

WSGI_APPLICATION = 'AquiSopas.wsgi.application'

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
if not os.getenv('HAS_DB'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('DATABASE_NAME','appdb'),
            'USER': os.getenv('DATABASE_USER','default'),
            'PASSWORD': os.getenv('DATABASE_PASSWD','password'),
            'HOST': os.getenv('MYSQL_SERVICE_HOST','localhost'),
            'PORT': os.getenv('MYSQL_SERVICE_PORT','3306')
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es_MX'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
if not os.getenv('HAS_DB'):
    STATIC_URL = 'https://storage.googleapis.com/bdelivery/static/'
else:
    STATIC_URL = '/static/'
    #STATIC_URL = '/static/'

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

GS_BUCKET_NAME = "bdelivery"

MEDIA_ROOT = os.path.join("/var/www",'media')

if not os.getenv('HAS_DB'):
    MEDIA_URL = 'https://storage.googleapis.com/bdelivery/cache/'
else:
    MEDIA_URL = '/media/'

OSCAR_HOMEPAGE = reverse_lazy("catalogue:index")

OSCAR_PRODUCTS_PER_PAGE = 14

OSCAR_HIDDEN_FEATURES = [
    'wishlists',
    'reviews'
]

OSCAR_GOOGLE_ANALYTICS_ID = "UA-110543293-1"

# EMAIL CONFIGURATION
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"

ANYMAIL = {
    "MAILGUN_API_KEY": "key-2627cb8e57c0efb4f85eaa918870517d",
    "MAILGUN_SENDER_DOMAIN": 'sac.aquisopas.com',  # your Mailgun domain, if needed
}

OSCAR_FROM_EMAIL = "web@aquisopas.com"

DEFAULT_FROM_EMAIL = "web@sac.aquisopas.com"  # if you don't already have this in settings

EMAIL_SUBJECT_PREFIX = "Orden Electronica"
