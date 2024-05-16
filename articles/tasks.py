from celery import shared_task
from celery.schedules import crontab
from articles.utils import fill_rate_ratios
from medium.celery import app as celery_app


@shared_task
def fill_rate_ratios_task():
	fill_rate_ratios()

celery_app.conf.beat_schedule = {
    'run-every-20-minutes': {
        'task': 'articles.tasks.fill_rate_ratios_task',
        'schedule': crontab(minute='*/20'), 
    },
}

