from .base import *
DEBUG = False
ADMINS = (
    ('PyGod', 'mickiasomg@gmail.com'),
)

ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com', '*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'pygod',
        'PASSWORD': '12345',
    }
}


SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
# HTTPS SETTINGS
# SECURE_HSTS_SECONDS = 31536000 # 1 YEAR
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE= True
# CSRF_COOKIE_SECURE = True
# Application definition
