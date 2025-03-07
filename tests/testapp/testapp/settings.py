from __future__ import absolute_import, unicode_literals

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import wagtail

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/


# Application definition
if wagtail.VERSION >= (2, 0):
    wagtail_apps = [
        'wagtail.contrib.forms',
        'wagtail.sites',
        'wagtail.users',
        'wagtail.admin',
        'wagtail.core',
        'wagtail.documents',
        'wagtail.images',
    ]
    wagtail_middlewares = [
        'wagtail.core.middleware.SiteMiddleware',
    ]
else:
    wagtail_apps = [
        'wagtail.wagtailforms',
        'wagtail.wagtailsites',
        'wagtail.wagtailusers',
        'wagtail.wagtaildocs',
        'wagtail.wagtailimages',
        'wagtail.wagtailadmin',
        'wagtail.wagtailcore',
    ]
    wagtail_middlewares = [
        'wagtail.wagtailcore.middleware.SiteMiddleware',
    ]

INSTALLED_APPS = wagtail_apps + [
    'home',

    'django_recaptcha',
    'wagtailcaptcha',

    'modelcluster',
    'taggit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
] + wagtail_middlewares

ROOT_URLCONF = 'testapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'testapp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'var', 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'var', 'media')
MEDIA_URL = '/media/'


# Wagtail settings

WAGTAIL_SITE_NAME = 'testapp'

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://example.com'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4*5e^@2%(h#$*b4=ze_kcdw46-$0z#rrf3661c5(&+x^oj=4)+'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *  # noqa: F401, F403
except ImportError:
    pass
