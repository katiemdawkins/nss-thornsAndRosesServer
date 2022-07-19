"""View for handling Retailer Requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from thornsNRosesAPI.models.retailer import Retailer
from thornsNRosesAPI.serializers.retailer_serializer import RetailerSerializer

class RetailerView(ViewSet):
    """Retailer View"""
    
    def retrieve(self,request, pk):
        """Handel GET Requests for Single Retailer"""
        try:
            retailer = Retailer.objects.get(pk=pk)
            serializer = RetailerSerializer(retailer)
            return Response (serializer.data, status=status.HTTP_200_OK)
        except Retailer.DoesNotExist as ex:
            return Response ({'message':ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self,request):
        """Handel GET Requests for All Nurseries"""
        retailers = Retailer.objects.all()
        serializer = RetailerSerializer(retailers, many= True)
        return Response (serializer.data, status=status.HTTP_200_OK)