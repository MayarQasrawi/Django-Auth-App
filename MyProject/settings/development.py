"""
Development settings
"""
from .base import *
from .database import DATABASES
from .auth import *
from .drf import *
from .logging import *

# Development overrides
DEBUG = True
ALLOWED_HOSTS = ["*"]


# Email in console (no SMTP needed in dev)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Optional: Debug toolbar
# INSTALLED_APPS += ["debug_toolbar"]
# MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
# INTERNAL_IPS = ["127.0.0.1"]
