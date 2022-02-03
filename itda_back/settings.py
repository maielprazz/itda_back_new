from pathlib import Path
import os
from dotenv import load_dotenv
import datetime
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType, LDAPSearchUnion

# load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i=p77-)mhwdjafcq^!%h%-*vp144@ljxbrw6970y8p6g1j83d9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = [
    'http://jkthomaasql03','localhost'
]
ALLOWED_HOSTS = ['jkthomaasql03','localhost','*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'corsheaders',
    'itda_front',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'api',
    'authentication',
    'useraccessmenu',
    'mod_wsgi.server',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'itda_back.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'itda_front/dist'),
        ],
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

WSGI_APPLICATION = 'itda_back.wsgi.application'

DATABASES = {
    
        'default': {
            'ENGINE': 'mssql',
            'NAME': 'DB_PORTAL',
            'HOST': 'JKTHOMAASQL03',
            'PORT': '1433',
            'OPTIONS': { 'DRIVER':'ODBC Driver 17 for SQL Server', 'dsn':'SQL03_PORTAL'},
        },

        'sql2': {
            'ENGINE': 'mssql',
            'NAME': 'DB_PM',
            'USER': 'userdbsql',
            'PASSWORD': 'Us3rdbsql',
            'HOST': 'JKTHOMAASQL02',
            'PORT': '1433',

            'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',
            },
        },
        'sql': {
            'ENGINE': 'mssql',
            'NAME': 'MAP',
            'USER': 'userdbsql',
            'PASSWORD': 'Us3rdbsql',
            'HOST': 'JKTHOMAASQL',
            'PORT': '1433',

            'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',
            },
        },
        'rds': {
            'ENGINE': 'mssql',
            'NAME': 'db_pm',
            'USER': 'maa_sql',
            'PASSWORD': 'MAAsql#admin#',
            'HOST': 'rm-d9jl51n4984b493ex.mssql.ap-southeast-5.rds.aliyuncs.com',
            'PORT': '1433',

            'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',
            },
        },
}

REST_FRAMEWORK = {
    # 'DEFAULT_RENDERER_CLASSES': [
    # 'rest_framework.renderers.JSONRenderer',
    # 'rest_framework.renderers.BrowsableAPIRenderer',
    # ],
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10,
    'COERCE_DECIMAL_TO_STRING' : False,
    'NON_FIELD_ERRORS_KEY': 'Error',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=4),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    # 'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': datetime.timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': datetime.timedelta(days=1),
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'authentication.User'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'muiadmin/build/static'),
    os.path.join(BASE_DIR, 'itda_front/dist'),
    # os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_USE_TLS= True
EMAIL_HOST=os.environ.get('EMAIL_HOST')
EMAIL_PORT=os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER=os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=os.environ.get('EMAIL_HOST_PASSWORD') 

############################### LDAP Settings #####################
# Baseline configuration.
AUTH_LDAP_SERVER_URI = 'ldap://map.co.id:389'#os.environ.get('LDAP_HOST_URI')

AUTH_LDAP_BIND_DN = "CN=ba admin,OU=ADMINS,OU=Functional Account,DC=map,DC=co,DC=id"
AUTH_LDAP_BIND_PASSWORD = "Password01"
AUTH_LDAP_USER_SEARCH = LDAPSearchUnion(
LDAPSearch("OU=Bigfix Deployment,OU=Users,OU=MAA,DC=map,DC=co,DC=id", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)"),
LDAPSearch("OU=ADMINS,OU=Functional Account,DC=map,DC=co,DC=id", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)"),
LDAPSearch("OU=Head Office,OU=Users,OU=MAA,DC=map,DC=co,DC=id", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)"),
LDAPSearch("OU=HO,OU=Users,OU=MAP,DC=map,DC=co,DC=id", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)"),
)

# LDAPSearch("OU=Bigfix Deployment,OU=Users,OU=MAA,DC=map,DC=co,DC=id", ldap.SCOPE_SUBTREE, "(cn=%(user)s)"),
# LDAPSearch("OU=Bigfix Deployment,OU=Users,OU=MAA,DC=map,DC=co,DC=id", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")
# LDAPSearch("OU=Head Office,OU=Users,OU=MAA,DC=map,DC=co,DC=id", ldap.SCOPE_SUBTREE, "(cn=%(user)s)"),
# OU=Stores,OU=MAA,DC=map,DC=co,DC=id
# OU=Store Ecomm,OU=MAA,DC=map,DC=co,DC=id


# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    "username": "sAMAccountName",
    "email": "mail",
    "employeeID" : "employeeID",
    "display_name" : "displayName",
}

# AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#     "is_active": "cn=active,ou=django,ou=groups,dc=example,dc=com",
#     "is_staff": "cn=staff,ou=django,ou=groups,dc=example,dc=com",
#     "is_superuser": "cn=superuser,ou=django,ou=groups,dc=example,dc=com",
# }

# This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True #True

# Use LDAP group membership to calculate group permissions.
# AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache distinguished names and group memberships for an hour to minimize
# LDAP traffic.
AUTH_LDAP_CACHE_TIMEOUT = 3600

# Keep ModelBackend around for per-user permissions and maybe a local
# superuser.
AUTHENTICATION_BACKENDS = (
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
)

