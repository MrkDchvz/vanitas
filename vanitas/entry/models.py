from django.db import models
from django.utils import timezone
# Create your models here.

class Mood(models.Model):
    name = models.CharField(max_length=200)
    emoji = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} {self.emoji}"


class Entry(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.mood.emoji} {self.title}"

 