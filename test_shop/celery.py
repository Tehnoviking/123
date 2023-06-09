import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE","test_shop.settings")
app = Celery("test_shop")
app.config_from_object("django.conf:settings",namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'every':{
        'task':'api.tasks.test_scheduled_task',
        'schedule':crontab()
    }
}