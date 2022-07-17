from django.db import models

class Flower(models.Model):
    color = models.CharField(max_length=25)
    species = models.CharField(max_length=25)