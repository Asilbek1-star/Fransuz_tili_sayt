from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Django settings modulini sozlash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Celery dasturini yaratish
app = Celery('fransuz_tili_sayt')

# Celery konfiguratsiyasini Django'niki bilan sozlash
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery vazifalarini avtomatik ravishda topish
app.autodiscover_tasks()
