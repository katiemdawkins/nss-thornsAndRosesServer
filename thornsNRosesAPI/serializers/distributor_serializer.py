from rest_framework import serializers
from thornsNRosesAPI.models.distributor import Distributor

class DistributorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Distributor
        fields = ("id", "business_name", "markup_percentage")