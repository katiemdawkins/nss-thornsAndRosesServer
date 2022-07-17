from rest_framework import serializers
from thornsNRosesAPI.models.nursery import Nursery

class NurserySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Nursery
        fields = ("id", "business_name")