from kaft_clone.settings.settings_base import INSTALLED_APPS
import os
from .settings_base import INSTALLED_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'muboys',
        'USER': 'murtekbey',
        'PASSWORD': 'murtek2Q122',
        'HOST': '160.153.128.44',
    }
}

INSTALLED_APPS += [
    'django_extensions',
]
