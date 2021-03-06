"""
Django settings for web_4 project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'empa)!a*nu)3@_+$#rr814f25k&x%fkum8oy)m1m$0s@4tu1&9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'ruzepelcovi.cz']

DEFAULT_FROM_EMAIL = 'pelc.it@gmail.com'

if DEBUG:
    EMAIL_USE_TLS = True
    SERVER_EMAIL = 'pelc.it@gmail.com'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'singh.pelc.it@gmail.com'
    EMAIL_HOST_PASSWORD = 'HeslonacaS'
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Application definition

INSTALLED_APPS = [
    'static_precompiler',
    'bootstrap4',
    'bootstrapform',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Shop.apps.ShopConfig',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',
    'sorl.thumbnail',
    'django.contrib.admin',
    'colorfield',
    'ckeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web_4.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'web_4.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        # TODO: Tu to bude chtít trochu poladit .mysql
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'USER':
        #'PASSWORD':
        #'HOST':
    }
}

# Needed django-allauth

AUTHENTICATION_BACKENDS = (
     # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_ADAPTER ='allauth.account.adapter.DefaultAccountAdapter'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "mandatory" #povinný |optional
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 21
SOCIALACCOUNT_ADAPTER = 'social_adapter.SocialAccountAdapter'
SOCIALACCOUNT_PROVIDERS = {
        'facebook': {
                'METHOD': 'js_sdk',
                'SCOPE': ['email', 'public_profile'],
                'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
                'INIT_PARAMS': {'cookie': True},
                'FIELDS': [
                    'id',
                    'email',
                    'name',
                    'first_name',
                    'last_name',
                    'verified',
                    'locale',
                    'timezone',
                    'link',
                    'gender',
                    'updated_time',
                ],
                'EXCHANGE_TOKEN': True,
                # 'LOCALE_FUNC': lambda request: return 'cs_CZ',
                # 'VERIFIED_EMAIL': False,
                # 'VERSION': 'v2.12',
            },
     # 'google':
     #    { 'SCOPE': ['profile', 'email'],
     #      'AUTH_PARAMS': { 'access_type': 'online' }}
    }

SITE_ID = 2

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'cs-cz'

TIME_ZONE = 'Europe/Prague'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
