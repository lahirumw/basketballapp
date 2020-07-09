from django.db import models
from django.db import models

# Create your models here.
class Match(models.Model):
    name = models.CharField(max_length=1000, default='')
    date = models.CharField(max_length=1000, default='')
    status = models.CharField(max_length=1000, default='')
    location = models.CharField(max_length=1000, default='')
    teams = models.CharField(max_length=20, default='')
    scores = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.name
# Create your models here.
