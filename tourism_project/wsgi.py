"""
WSGI config for tourism_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourism_project.settings')

application = get_wsgi_application()
# application = WhiteNoise(application)
# application.add_files(" os.path.join(BASE_DIR, 'static')", prefix="more-files")
