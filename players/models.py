from django.db import models


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=1000, blank=False)
    team = models.IntegerField(blank=False)
    country = models.CharField(max_length=10, blank=False)
    birthday = models.DateField()
    age = models.PositiveIntegerField()
    debut = models.CharField(max_length=50, blank=False)
    experience = models.PositiveIntegerField()
    position = models.CharField(max_length=50, blank=False)
    shoot = models.CharField(max_length=50, blank=False)
    matches = models.PositiveIntegerField()
    rank = models.PositiveIntegerField()
    image = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
