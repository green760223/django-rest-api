"""
WSGI config for django_rest_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_rest_api.settings")

application = get_wsgi_application()
application = WhiteNoise(
    application, root=os.path.join(os.path.dirname(__file__), "staticfiles")
)
