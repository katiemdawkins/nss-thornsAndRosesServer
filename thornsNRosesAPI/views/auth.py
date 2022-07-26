from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from thornsNRosesAPI.models.thornUser import ThornUser


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles the authentication of a user

    Method arguments:
    request -- The full HTTP request object
    '''
    username = request.data['username']
    password = request.data['password']

    authenticated_user = authenticate(username=username, password=password)

    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        
        data = {
            'valid': True,
            'token': token.key
        }
    else:
        data = { 'valid': False }
    return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new gamer for authentication

    Method arguments:
    request -- The full HTTP request object
    '''

    
    new_user = User.objects.create_user(
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        email=request.data['email'],
        username=request.data['username'],
        password=request.data['password'],
    )

    
    thorn_user = ThornUser.objects.create(
        user= new_user,
        distributor_employee=request.data['distributor_employee'],
        nursery_employee = request.data['nursery_employee'],
        retail_employee = request.data['retail_employee'],
        event_planner = request.data['event_planner']
    )
    
    token = Token.objects.create(user=thorn_user.user)
    
    
    data = { 'token': token.key }
    return Response(data, status=status.HTTP_201_CREATED)