from django.db import models

class Distributor(models.Model):
    business_name = models.CharField(max_length=25)
    markup_percentage = models.IntegerField()