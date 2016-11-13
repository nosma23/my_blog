import os
from django.conf import settings

if not settings.DEBUG:
    INSTALLED_APPS = [
        # django apps
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.sites',
        'django.contrib.staticfiles',
        # third party apps
        'crispy_forms',
        'ckeditor',
        'disqus',
        'markdown_deux',
        'storages',
        # my apps
        'blog',
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
        }
    }

    try:
        import dj_database_url
        db_from_env = dj_database_url.config(conn_max_age=500)
        DATABASES['default'].update(db_from_env)
    except:
        pass

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    ALLOWED_HOSTS = ['radiant-ocean-78501.herokuapp.com', 'www.lifeproficiency.com']

    AWS_ACCESS_KEY_ID = "AKIAI6BF7LNPE2YDDGAQ"
    AWS_SECRET_ACCESS_KEY = "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"

    AWS_FILE_EXPIRE = 200
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

    import datetime

    two_months = datetime.timedelta(days=61)
    date_two_months_later = datetime.date.today() + two_months
    expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

    AWS_HEADERS = {
        'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
    }

    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'manos.bass23@gmail.com'
    EMAIL_HOST_PASSWORD = 'lolol456'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
