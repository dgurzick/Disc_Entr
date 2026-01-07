"""
WSGI config for disc_entr_project project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'disc_entr_project.settings')

application = get_wsgi_application()
