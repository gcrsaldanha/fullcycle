from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-*@f%k!+c^6mnp9*rn_x*#j%x1_2)$)f$47#%8m%fbfoc198fao'  # TODO: read from env var/vault

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # TODO: Keeping this for simplicity, should be set to False when service is deployed

ALLOWED_HOSTS = ['*']  # TODO: Change this when service is deployed


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'inventory',
    'django_extensions',
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

ROOT_URLCONF = 'stock_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'stock_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
# }

DATABASES = {
    # TODO: configuration should come from env vars
    "default": {
        "NAME": "inventory_db",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "postgres_db",  # docker-compose service name
        "PORT": 5432,
        "ENGINE": "django.db.backends.postgresql",
        "ATOMIC_REQUESTS": True,
        "OPTIONS": {"application_name": "stock_system"},
    },
    # Had too much trouble configuring MySQL, so I'm using Postgres for now
    # 'mysql': {
    #     'NAME': 'inventory_db',
    #     # 'ENGINE': 'mysql.connector.django',  # using MySQL connector https://dev.mysql.com/doc/connector-python/en/connector-python-django-backend.html
    #     # 'ENGINE': 'django.db.backends.mysql',  # Django's recommended choice
    #     # 'HOST': '127.0.0.1',
    #     'HOST': 'db',  # TODO: read from env var
    #     'PORT': 3306,
    #     'USER': 'admin',
    #     'PASSWORD': 'admin',
    #     'OPTIONS': {
    #       'autocommit': True,
    #       'use_oure': True,
    #       'init_command': "SET foo='bar';"
    #     },
    # }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 15,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
}
