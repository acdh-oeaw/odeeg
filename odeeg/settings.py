import os
from pathlib import Path


ACDH_IMPRINT_URL = (
    "https://shared.acdh.oeaw.ac.at/acdh-common-assets/api/imprint.php?serviceID="
)
REDMINE_ID = 11625
SECRET_KEY = os.environ.get("SECRET_KEY", "rlYWFQbF")
ARCHE_BG = "https://arche.acdh.oeaw.ac.at/blazegraph/sparql"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent


ADD_ALLOWED_HOST = os.environ.get("ALLOWED_HOST", "*")
ALLOWED_HOSTS = [
    "127.0.0.1",
    "0.0.0.0",
    ADD_ALLOWED_HOST,
]
if os.environ.get("DEBUG"):
    DEBUG = True
else:
    DEBUG = False

# Application definition

INSTALLED_APPS = [
    "dal",
    "django.contrib.admin",
    "dal_select2",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "reversion",
    "haystack",
    "leaflet",
    "crispy_forms",
    "django_filters",
    "django_tables2",
    "rest_framework",
    "webpage",
    "browsing",
    "charts",
    "vocabs",
    "vases",
    "netvis",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "odeeg"),
        "USER": os.environ.get("POSTGRES_USER", "postgres"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "postgres"),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTEGRES_PORT", "5432"),
    }
}


HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
        "PATH": os.path.join(BASE_DIR, "whoosh_index"),
    },
}

CRISPY_TEMPLATE_PACK = "bootstrap4"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "reversion.middleware.RevisionMiddleware",
]

ROOT_URLCONF = "odeeg.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "webpage.webpage_content_processors.installed_apps",
                "webpage.webpage_content_processors.is_dev_version",
                "webpage.webpage_content_processors.get_db_name",
            ],
        },
    },
]

WSGI_APPLICATION = "odeeg.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = "/media/"

ARCHE_SETTINGS = {
    "project_name": ROOT_URLCONF.split(".")[0],
    "base_url": "https://id.acdh.oeaw.ac.at/{}".format(ROOT_URLCONF.split(".")[0]),
}

VOCABS_DEFAULT_PEFIX = os.path.basename(BASE_DIR)

VOCABS_SETTINGS = {
    "default_prefix": VOCABS_DEFAULT_PEFIX,
    "default_ns": "http://www.vocabs/{}/".format(VOCABS_DEFAULT_PEFIX),
    "default_lang": "en",
}

LEAFLET_CONFIG = {
    "MAX_ZOOM": 18,
    "DEFAULT_CENTER": (37, 23),
    "DEFAULT_ZOOM": 6,
    "TILES": [
        (
            "BASIC",
            "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
            {
                "attribution": '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>\
                    contributors',
                "maxZoom": 18,
            },
        )
    ],
}

ARCHE_BASE = "https://arche.acdh.oeaw.ac.at"
ARCHE_SEARCH = f"{ARCHE_BASE}/api/search"
ARCHE_NS = "https://vocabs.acdh.oeaw.ac.at/schema%23"
ARCHE_ID_PROP = "https://vocabs.acdh.oeaw.ac.at/schema#hasIdentifier"


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "my_cache_table",
        "TIMEOUT": None,
        "OPTIONS": {"MAX_ENTRIES": 1000},
    }
}