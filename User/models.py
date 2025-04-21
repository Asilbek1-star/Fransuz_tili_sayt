from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    level = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return self.name

    def total_score(self):
        return sum(result.score for result in self.testresult_set.all())

class TestResult(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.name} - {self.score}"

class Video(models.Model):
    LEVEL_CHOICES = [
        ('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'),
        ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'),
        ('C1', 'C1'),
    ]

    CATEGORY_CHOICES = [
        ('grammar', 'Grammar'),
        ('vocabulary', 'Vocabulary'),
        ('listening', 'Listening'),
        ('speaking', 'Speaking'),
        ('writing', 'Writing'),
    ]

    title = models.CharField(max_length=200)
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='A1')
    video_file = models.FileField(upload_to='videos/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='grammar')
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    thumbnail = models.ImageField(upload_to='video_thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return self.name