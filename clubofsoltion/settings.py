from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h%y_ejtezu9vq%bx#1weelibbs&9rup^o$q3nik8z49034_ay('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # External
    'django.contrib.sites',
    #########
    'main',
    'admin_panel',
    'location_manager',
    'payment_manager',
    # External
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    
    'conference.apps.ConferenceConfig',
    'channels',

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

ROOT_URLCONF = 'clubofsoltion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'clubofsoltion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
static_root = BASE_DIR / 'static'

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / 'media'


STATICFILES_DIRS = [
    BASE_DIR / "static",
    '/var/www/static/',
]

AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'social_core.backends.google.GoogleOAuth2',
]

SITE_ID = 1
LOGIN_REDIRECT_URL = '/Admin/Dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = '/'

SOCIALACCOUNT_PROVIDERS = {
    'google':{
        'SCOPE':[
            'profile',
            'email',
        ],
        'AUTH_PARAMS':{
            'access_type':'online',
        }
    },
    'facebook':
        {
         'METHOD': 'oauth2',
         'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
         'SCOPE': ['email', 'public_profile'],
         'INIT_PARAMS': {'cookie': True},
         'FIELDS': [
             'id',
             'first_name',
             'last_name',
             'name',
             'name_format',
             'picture',
             'short_name'
         ],
         'EXCHANGE_TOKEN': True,
         'LOCALE_FUNC': lambda request: 'ru_RU',
         'VERIFIED_EMAIL': False,
         'VERSION': 'v7.0',
         # you should fill in 'APP' only if you don't create a Facebook instance at /admin/socialaccount/socialapp/
         'APP': {
             'client_id': '488279085558388',  # !!! THIS App ID
             'secret': 'd35f243578d343ad7ad959ddd9abb982',  # !!! THIS App Secret
             'key': ''
                }
         }
}
# SOCIAL_AUTH_FACEBOOK_KEY = '488279085558388'
# SOCIAL_AUTH_FACEBOOK_SECRET = 'd35f243578d343ad7ad959ddd9abb982'

DATETIME_FORMAT= "%Y-%m-%d %H:%M:%S"
L10N = False
USE_TZ = False


# Channels
ASGI_APPLICATION = 'clubofsoltion.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}