"""View for handling Nursery Requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from thornsNRosesAPI.models.nursery import Nursery
from thornsNRosesAPI.serializers.nursery_serializer import NurserySerializer

class NurseryView(ViewSet):
    """Nursery View"""
    
    def retrieve(self,request, pk):
        """Handel GET Requests for Single Nursery"""
        try:
            nursery = Nursery.objects.get(pk=pk)
            serializer = NurserySerializer(nursery)
            return Response (serializer.data, status=status.HTTP_200_OK)
        except Nursery.DoesNotExist as ex:
            return Response ({'message':ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self,request):
        """Handel GET Requests for All Nurseries"""
        nurseries = Nursery.objects.all()
        serializer = NurserySerializer(nurseries, many= True)
        return Response (serializer.data, status=status.HTTP_200_OK)