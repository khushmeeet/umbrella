from .settings import *

SECRET_KEY = 'something'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'umb_test',
        'USER': 'postgres',
        'PASSWORD': 'test123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEBUG = True
