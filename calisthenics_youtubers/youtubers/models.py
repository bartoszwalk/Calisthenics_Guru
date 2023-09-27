from django.db import models

# Create your models here.
class Youtuber(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    subscribers = models.IntegerField()
    link = models.URLField(max_length=200)
    image = models.ImageField(default = 'placeholder.png', blank=True)

    def __str__(self):
        return self.title