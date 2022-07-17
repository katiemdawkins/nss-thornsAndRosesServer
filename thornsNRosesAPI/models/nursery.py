from django.db import models

class Nursery(models.Model):
    business_name = models.CharField(max_length=30)
    