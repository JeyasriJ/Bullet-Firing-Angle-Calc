"""
ASGI config for bullet_calculator project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bullet_calculator.settings')

application = get_asgi_application()
