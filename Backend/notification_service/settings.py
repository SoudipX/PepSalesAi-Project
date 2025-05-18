INSTALLED_APPS = [
    ...
    'notifications',
    'rest_framework',
]

CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'