from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    level = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Video(models.Model):
    LEVEL_CHOICES = [
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
    ]
    title = models.CharField(max_length=200)  # Video nomi
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='A1')  # Ingliz tili darajasi
    video_file = models.FileField(upload_to='videos/')  # Video fayl

    def __str__(self):
        return self.title





