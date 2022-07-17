"""View for handling Distributor Requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from thornsNRosesAPI.models.distributor import Distributor
from thornsNRosesAPI.serializers.distributor_serializer import DistributorSerializer