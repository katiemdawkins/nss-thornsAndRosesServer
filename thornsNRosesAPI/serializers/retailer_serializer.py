from rest_framework import serializers
from thornsNRosesAPI.models.retailer import Retailer

class RetailerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Retailer
        fields = ("id", "business_name", "address", "markup_percentage", "distributor")
        depth = 1