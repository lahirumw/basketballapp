from django.db import models

# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=1000, default='')
    year = models.CharField(max_length=1000, default='')
    teams = models.CharField(max_length=1000, default='')
    trophy = models.CharField(max_length=1000, default='')
    Country = models.CharField(max_length=20, default='')
    winner = models.CharField(max_length=1000, default='')
    runnerUp = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.name