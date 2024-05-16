import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medium.settings')
app = Celery('medium')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

