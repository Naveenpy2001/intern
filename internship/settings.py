"""
Django settings for internship project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4_6-7rxf_g07s7h_sy#2js)^6uq=b(zjb8gh3s7dcgu2g-pi1k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ["intern.tsaritservices.com"]
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app'
]


AUTH_USER_MODEL = 'app.CustomUser'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'internship.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'internship.wsgi.application'




# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

<<<<<<< HEAD
=======
<<<<<<< HEAD
#DATABASES = {
#    'default': {
#       'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'demo',        # Replace 'your_database_name' with your actual database name
#        'USER': 'root',       # Replace 'your_mysql_username' with your MySQL username
#        'PASSWORD': 'root',   # Replace 'your_mysql_password' with your MySQL password
#        'HOST': 'localhost',                 # Replace 'localhost' with your MySQL host if it's not running locally
#        'PORT': '3306', 
#    }
    # 'default': {
    #    'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'fikwzpdr_intern',        # Replace 'your_database_name' with your actual database name
    #     'USER': 'fikwzpdr_intern',       # Replace 'your_mysql_username' with your MySQL username
    #     'PASSWORD': 'Tsarit@12345',   # Replace 'your_mysql_password' with your MySQL password               
    #     'PORT': '3306',  
    # }
#}

=======
# DATABASES = {
#     'default': {
#        'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'intern',        # Replace 'your_database_name' with your actual database name
#         'USER': 'root',       # Replace 'your_mysql_username' with your MySQL username
#         'PASSWORD': 'root',   # Replace 'your_mysql_password' with your MySQL password
#         'HOST': 'localhost',                 # Replace 'localhost' with your MySQL host if it's not running locally
#         'PORT': '3306', 
#     }
# }
>>>>>>> 0244c9a0709a14339734634d49541dbcc0766af2

>>>>>>> 0c1fd01fedbb4000a8129d725f007323cc6ffe7e
DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.mysql',
        'NAME': 'internnn',        # Replace 'your_database_name' with your actual database name
        'USER': 'root',       # Replace 'your_mysql_username' with your MySQL username
        'PASSWORD': 'root',   # Replace 'your_mysql_password' with your MySQL password
        'HOST': 'localhost',                 # Replace 'localhost' with your MySQL host if it's not running locally
        'PORT': '3306', 
    }
}

<<<<<<< HEAD
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

=======
<<<<<<< HEAD


=======
>>>>>>> 0244c9a0709a14339734634d49541dbcc0766af2
>>>>>>> 0c1fd01fedbb4000a8129d725f007323cc6ffe7e
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

TIME_ZONE = 'Asia/Kolkata'


USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles'),
]

<<<<<<< HEAD
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
=======
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'your_app.backends.EmailAuthBackend',  # Add your custom backend
)

>>>>>>> 0244c9a0709a14339734634d49541dbcc0766af2

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tsaritservices@gmail.com'  # Your Gmail email address
EMAIL_HOST_PASSWORD = 'usan aphb mlpf itjx'     # Your Gmail password or App Password
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

