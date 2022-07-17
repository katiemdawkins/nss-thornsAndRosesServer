"""View for handling Retailer Requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from thornsNRosesAPI.models.retailer import Retailer
from thornsNRosesAPI.serializers.retailer_serializer import RetailerSerializer