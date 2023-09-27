from django.db import models
import datetime

class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    bodytext = models.TextField('Page Content', blank=True)

    def __str__(self):
        return self.title
