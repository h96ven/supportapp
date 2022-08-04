import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'supportapp.settings')

celery = Celery('supportapp')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()
