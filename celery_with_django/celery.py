from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE','celery_with_django.settings')

app = Celery('celery_with_django')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# Celery beat settings

app.conf.beat_schedule ={

    'Task_to_print_hello':{
        'task' : 'mainapp.tasks.print_hello',
        'schedule' : crontab(hour=9, minute=36),

    },
    'Task_to_print_hello_for_every_minute':{
        'task': 'mainapp.tasks.print_hello',
        'schedule': crontab(minute='*/1'),

    }
    }


app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')