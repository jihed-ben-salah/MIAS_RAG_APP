"""ASGI entrypoint placeholder for saipro_project."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "saipro_project.settings.dev")

application = get_asgi_application()
