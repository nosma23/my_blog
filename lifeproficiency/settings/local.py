import os
from django.conf import settings

DEBUG = True

SITE_ID = 1

INSTALLED_APPS = [
    #django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    #third party apps
    'crispy_forms',
    'ckeditor',
    'markdown_deux',
    #my apps
    'blog',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]


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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#DEFAULT_FROM_EMAIL = 'testing@example.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'manos.bass23@gmail.com'
EMAIL_HOST_PASSWORD = 'lolol456'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

CRISPY_TEMPLATE_PACK = 'bootstrap3'

AWS_ACCESS_KEY_ID = "AKIAI6BF7LNPE2YDDGAQ"
AWS_SECRET_ACCESS_KEY = "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"


AWS_FILE_EXPIRE = 20000
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'lifeproficiency.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'lifeproficiency.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'lifedjango'
S3DIRECT_REGION = 'us-west-2'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
AWSS3HOST = "s3-us-west-2.amazonaws.com"

import datetime

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}