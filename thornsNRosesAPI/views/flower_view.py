"""View for handling Flower Requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from thornsNRosesAPI.models.flower import Flower
from thornsNRosesAPI.serializers.flower_serializer import FlowerSerializer

class FlowerView(ViewSet):
    """Flower View"""
    
    def retrieve(self,request, pk):
        """Handel GET Requests for Single Flower"""
        try:
            flower = Flower.objects.get(pk=pk)
            serializer = FlowerSerializer(flower)
            return Response (serializer.data, status=status.HTTP_200_OK)
        except Flower.DoesNotExist as ex:
            return Response ({'message':ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self,request):
        """Handel GET Requests for All Flowers"""
        flowers = Flower.objects.all()
        serializer = FlowerSerializer(flowers, many= True)
        return Response (serializer.data, status=status.HTTP_200_OK)

            