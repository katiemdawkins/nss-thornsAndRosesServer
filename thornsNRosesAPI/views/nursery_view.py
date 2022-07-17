"""View for handling Nursery Requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from thornsNRosesAPI.models.nursery import Nursery
from thornsNRosesAPI.serializers.nursery_serializer import NurserySerializer