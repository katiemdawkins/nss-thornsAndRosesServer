from rest_framework import serializers
from thornsNRosesAPI.models.nurseryFlowerPrice import NurseryFlowerPrice

class NurseryFlowerPriceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NurseryFlowerPrice
        fields = ("id", "nursery", "flower", "distributor", "price")
        depth = 1