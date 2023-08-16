from base import *  # noqa

SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")  # noqa
STATIC_ROOT = env("STATIC_ROOT")  # noqa

CSRF_COOKIE = True
SESSION_COOKIE_SECURE = True
CORS_ALLOWED_ORIGINS = env.list(  # noqa
    "CORS_ALLOWED_ORIGINS",
    default=[]
)

REST_FRAMEWORK = {  # noqa
    **REST_FRAMEWORK,  # noqa
    'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer']
}  # noqa
