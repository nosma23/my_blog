"""
WSGI config for lifeproficiency project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lifeproficiency.settings")

application = get_wsgi_application()

if not settings.DEBUG:
    try:
        from whitenoise.django import DjangoWhiteNoise
        application = DjangoWhiteNoise(get_wsgi_application())
    except:
        pass
