from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=1000, default='')
    country = models.CharField(max_length=20, default='')
    won = models.PositiveIntegerField(default=0)
    lost = models.PositiveIntegerField(default=0)
    matches = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)
    coach = models.CharField(max_length=1000, default='')
    executive = models.CharField(max_length=1000, default='')
    captain = models.CharField(max_length=1000, default='')
    flag = models.CharField(max_length=1000, default='')
    players = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.name
