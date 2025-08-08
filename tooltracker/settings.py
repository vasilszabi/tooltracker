import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# ... ostatné nastavenia ...

# Šablóny – aby Django našlo priečinok 'templates' v koreňi
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # <— toto pridaj/nezabudni
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

# Statické súbory
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]     # kde máš vlastné CSS/JS
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')       # kam sa zbalí pre produkciu

# Whitenoise na Render (servovanie statiky)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',         # <— vlož hneď po Security
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Uistime sa, že hosty sú povolené
ALLOWED_HOSTS = ["*"]
