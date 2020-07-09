from django.db import models

# Create your models here.
class Tournament(models.Model):

    def __str__(self):
        return self.name