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
        'markdown_deux',
        # my apps
        'blog',
    ]


    try:
        import dj_database_url
        db_from_env = dj_database_url.config(conn_max_age=500)
        DATABASES['default'].update(db_from_env)
    except:
        pass

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    ALLOWED_HOSTS = ['radiant-ocean-78501.herokuapp.com', 'www.lifeproficiency.com']

    STATIC_ROOT = os.path.join(settings.BASE_DIR, 'blog/static_cdn')
    MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'blog/media_cdn')

    STATICFILES_DIRS = [
        os.path.join(settings.BASE_DIR, "blog/static"),
        #'/var/www/static/',
    ]