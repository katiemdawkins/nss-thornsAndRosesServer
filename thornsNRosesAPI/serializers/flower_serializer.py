from rest_framework import serializers
from thornsNRosesAPI.models.flower import Flower

class FlowerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Flower
        fields = ("id", "color", "species")