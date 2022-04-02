from base import *  # noqa

SECURE_SSL_REDIRECT = True
STATIC_ROOT = env("STATIC_ROOT")

CSRF_COOKIE = True
SESSION_COOKIE_SECURE = True
CORS_ALLOWED_ORIGINS = env.list(
    "CORS_ALLOWED_ORIGINS",
    default=[]
)

REST_FRAMEWORK = {**REST_FRAMEWORK,
                  'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer']
                  }
