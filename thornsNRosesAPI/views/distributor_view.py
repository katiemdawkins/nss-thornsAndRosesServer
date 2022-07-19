"""View for handling Distributor Requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from thornsNRosesAPI.models.distributor import Distributor
from thornsNRosesAPI.serializers.distributor_serializer import DistributorSerializer

class DistributorView(ViewSet):
    """Distributor View"""
    
    def retrieve(self,request, pk):
        """Handel GET Requests for Single Distributor"""
        try:
            distributor = Distributor.objects.get(pk=pk)
            serializer = DistributorSerializer(distributor)
            return Response (serializer.data, status=status.HTTP_200_OK)
        except Distributor.DoesNotExist as ex:
            return Response ({'message':ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self,request):
        """Handel GET Requests for All Nurseries"""
        distributors = Distributor.objects.all()
        serializer = DistributorSerializer(distributors, many= True)
        return Response (serializer.data, status=status.HTTP_200_OK)