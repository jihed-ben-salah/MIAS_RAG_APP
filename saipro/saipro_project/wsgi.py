"""WSGI entrypoint placeholder for saipro_project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "saipro_project.settings.dev")

application = get_wsgi_application()
