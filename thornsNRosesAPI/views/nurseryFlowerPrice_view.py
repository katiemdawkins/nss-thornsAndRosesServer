"""View for handling Nursery Flower Prices Requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from thornsNRosesAPI.models.nurseryFlowerPrice import NurseryFlowerPrice
from thornsNRosesAPI.serializers.nurseryFlowerPrice_serializer import NurseryFlowerPriceSerializer

class NurseryFlowerPriceView(ViewSet):
    """Retailer View"""
    
    def retrieve(self,request, pk):
        """Handel GET Requests for Single Retailer"""
        try:
            nurseryFlowerPrice = NurseryFlowerPrice.objects.get(pk=pk)
            serializer = NurseryFlowerPriceSerializer(nurseryFlowerPrice)
            return Response (serializer.data, status=status.HTTP_200_OK)
        except NurseryFlowerPrice.DoesNotExist as ex:
            return Response ({'message':ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self,request):
        """Handel GET Requests for All Nurseries"""
        nurseryFlowerPrices = NurseryFlowerPrice.objects.all()
        
        distributor = request.query_params.get('distributor', None)
        flower = request.query_params.get('flower', None)
        nursery = request.query_params.get('nursery', None)
        
        if distributor is not None:
            nurseryFlowerPrices = nurseryFlowerPrices.filter(distributor__id = distributor)
            
        if flower is not None:
            nurseryFlowerPrices = nurseryFlowerPrices.filter(flower__id=flower)
            
        if nursery is not None:
            nurseryFlowerPrices = nurseryFlowerPrices.filter(nursery__id = nursery)
            
        serializer = NurseryFlowerPriceSerializer(nurseryFlowerPrices, many= True)
        return Response (serializer.data, status=status.HTTP_200_OK)