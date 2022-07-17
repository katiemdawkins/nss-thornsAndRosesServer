from django.db import models

class NurseryFlowerPrice(models.Model):
    nursery = models.ForeignKey("Nursery", on_delete=models.CASCADE)
    flower = models.ForeignKey("Flower", on_delete=models.CASCADE)
    distributor = models.ForeignKey("Distributor", on_delete=models.CASCADE)
    price = models.IntegerField()