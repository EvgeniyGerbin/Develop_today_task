import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'develops_today_task.settings')

app = Celery('develop_today_task')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'api.tasks.upvote_reset',
        'schedule': crontab(minute=1, hour=0)
    },
}