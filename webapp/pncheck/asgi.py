"""
ASGI config for pncheck project.
It exposes the ASGI callable as a module-level variable named ``application``.
Routers Used: We suggest that you have a ProtocolTypeRouter as the root application of your project - the one that you pass to protocol servers - and nest other, more protocol-specific routing underneath there.

For more information on this file, see

https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/

"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pncheck.settings')

application = get_asgi_application()


