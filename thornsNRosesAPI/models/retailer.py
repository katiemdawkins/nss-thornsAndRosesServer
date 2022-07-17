from django.db import models

class Retailer(models.Model):
    business_name = models.CharField(max_length=25)
    address = models.CharField(max_length=150)
    markup_percentage = models.IntegerField()
    distributor= models.ForeignKey("Distributor", on_delete=models.CASCADE)