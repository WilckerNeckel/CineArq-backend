
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = bool(os.environ.get("DEBUG"))
# SECRET_KEY = 'django-insecure-d$!p+5ro=12xlg(#-bjt8l9nyv6+d02_3hh*-^%$-#ke+zvbx&'
# DEBUG = True

BASE_DIR = Path(__file__).resolve().parent.parent
IS_DB_PRODUCTION = bool(os.environ.get("IS_DB_PRODUCTION"))


# ALLOWED_HOSTS = ['http://localhost', 
#                  "127.0.0.1", 
#                  "cinearqmt.com.br", 
#                  "www.cinearqmt.com.br", 
#                  "api.cinearqmt.com.br", 
#                  "www.api.cinearqmt.com.br",
#                 "https://api.cinearqmt.com.br",
#                 "https://www.api.cinearqmt.com.br",
#                 ]

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'login',
    'rest_framework_simplejwt',
    'corsheaders',
    'worksheet',
    'formulario',
    'area_admin',
    
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'setup.urls'

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

WSGI_APPLICATION = 'setup.wsgi.application'

if IS_DB_PRODUCTION:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'djangoreact',
            'USER': 'postgres',
            'PASSWORD': 'Admin@123Postgres',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
    
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# DATABASES = {
#     'default': {
#     'ENGINE': 'django.db.backends.sqlite3',
#     'NAME': BASE_DIR / 'db.sqlite3',
#         }
# }
            

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



LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Cuiaba'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DRF
REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}
JWT_ACCESS_TOKEN_LIFETIME = 3600
# authentication_backends serve para dizer ao django que ele deve usar o model de autenticação padrão
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_WHITELIST = ['*']

# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:8080',
#     'http://127.0.0.1:8080',
#     'cinearqmt.com.br',
#     'https://cinearqmt.com.br',
#     "https://api.cinearqmt.com.br",
#     "https://www.api.cinearqmt.com.br",
#     "api.cinearqmt.com.br"
#     "www.api.cinearqmt.com.br"
# ]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

