"""
Database configuration settings (PostgreSQL)
"""
from decouple import config

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",   # PostgreSQL backend
        "NAME": config("DB_NAME", default="postgres"),   # database name
        "USER": config("DB_USER", default="postgres"),   # username
        "PASSWORD": config("DB_PASSWORD", default=""),   # password
        "HOST": config("DB_HOST", default="localhost"),  # host (local)
        "PORT": config("DB_PORT", default="5432", cast=int),  # port
        "CONN_MAX_AGE": 60,  # persistent connections
        "OPTIONS": {
            "connect_timeout": 10,  # timeout in seconds
        },
    }
}
