from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Django project setting
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('fransuz_tili_sayt')

# Redis broker url
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
    broker_url='redis://redis:6379/0',  # Redis server URI
    result_backend='redis://redis:6379/0',  # Celery task natijalari uchun
)

app.autodiscover_tasks()
