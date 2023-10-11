"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*bub=uy6-%$t9hhlbgs45&vpb!kjk3^rk7bm^kyxda_lyqnyo_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'storages',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {    
    #local:
    # 'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': BASE_DIR / 'db.sqlite3',}

    # postgres public:
    'default': {'ENGINE': 'django.db.backends.postgresql','NAME': os.getenv("PUBLIC_NAME"),'USER': os.getenv("PUBLIC_USER"),'PASSWORD': os.getenv("PUBLIC_PASSWORD"),'HOST': os.getenv("PUBLIC_HOST"),'PORT': os.getenv("PUBLIC_PORT")}
}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#  ██████╗ ██████╗      ██╗███████╗ ██████╗████████╗    ███████╗████████╗ ██████╗ ██████╗  █████╗  ██████╗ ███████╗
# ██╔═══██╗██╔══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔══██╗██╔════╝ ██╔════╝
# ██║   ██║██████╔╝     ██║█████╗  ██║        ██║       ███████╗   ██║   ██║   ██║██████╔╝███████║██║  ███╗█████╗  
# ██║   ██║██╔══██╗██   ██║██╔══╝  ██║        ██║       ╚════██║   ██║   ██║   ██║██╔══██╗██╔══██║██║   ██║██╔══╝  
# ╚██████╔╝██████╔╝╚█████╔╝███████╗╚██████╗   ██║       ███████║   ██║   ╚██████╔╝██║  ██║██║  ██║╚██████╔╝███████╗
#  ╚═════╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝       ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                                                                                                 

STORAGES = {"default": {"BACKEND": "storages.backends.s3boto3.S3Boto3Storage"}}
AWS_S3_ENDPOINT_URL = os.getenv("LIARA_ENDPOINT")
AWS_S3_ACCESS_KEY_ID = os.getenv("LIARA_ACCESS_KEY")
AWS_S3_SECRET_ACCESS_KEY = os.getenv("LIARA_SECRET_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("LIARA_BUCKET_NAME")

# ██████╗ ███████╗███████╗████████╗
# ██╔══██╗██╔════╝██╔════╝╚══██╔══╝
# ██████╔╝█████╗  ███████╗   ██║   
# ██╔══██╗██╔══╝  ╚════██║   ██║   
# ██║  ██║███████╗███████║   ██║   
# ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   
                                 
                                 

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated',]
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny',]
    # 'DEFAULT_PERMISSION_CLASSES': ( 'rest_framework.permissions.IsAdminUser', ),
    
}

CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_ALLOW_ALL = False
# CORS_ORIGIN_WHITELIST = ('http://localhost:8000',)


# LOGIN_REDIRECT_URL = "login"
# LOGOUT_REDIRECT_URL = "login"
# SIGNUP_REDIRECT_URL = "home"