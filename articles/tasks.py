from celery import shared_task
from celery.schedules import crontab
from articles.utils import find_influenced_ratings
from medium.celery import app as celery_app


@shared_task
def find_influenced_ratings_task():
	find_influenced_ratings()

celery_app.conf.beat_schedule = {
    'run-every-30-minutes': {
        'task': 'articles.tasks.fill_rate_ratios_task',
        'schedule': crontab(minute='*/30'),
    },
}

