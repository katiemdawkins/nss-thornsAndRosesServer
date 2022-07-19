from django.db import models
from django.contrib.auth.models import User

class ThornUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    distributor_employee = models.BooleanField()
    nursery_employee = models.BooleanField()
    retail_employee = models.BooleanField()
    event_planner = models.BooleanField()