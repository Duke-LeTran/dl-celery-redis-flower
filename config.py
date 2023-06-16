# Example configuration file

# Flask configuration
DEBUG = True
SECRET_KEY = 'your_secret_key'

# Celery configuration
## https://docs.celeryq.dev/en/stable/userguide/configuration.html#std-setting-task_serializer
CELERY_BROKER_URL = 'redis://192.168.128.2:6379/0'  # Redis as broker
CELERY_RESULT_BACKEND = 'redis://192.168.128.2:6379/0'  # Redis as result backend
CELERY_IGNORE_RESULT = True
CELERY_RESULT_SERIALIZER = 'json' #default
CELERY_RESULT_SERIALIZER = 'json' #default
CELERY_ACCEPT_CONTENT = ['json'] #default, other e.g., actual content-type(MIME) ['application/json']
CELERY_ENABLE_UTC = True # default, if timezone not set
CELERY_TIMEZONE = 'America/Los_Angeles'

