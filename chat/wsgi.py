"""
WSGI config for chat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')

application = get_default_application()
