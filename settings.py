import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),  # This should match the service name in docker-compose
        'PORT': os.getenv('DB_PORT'),
    }
}
ALLOWED_HOSTS = ['*']