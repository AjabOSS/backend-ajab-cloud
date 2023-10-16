from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from myuser.models import MyUser
from .serializers import *


class UserRegisterAPI(APIView):
    def post(self, request):

        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            user = ser_data.create(ser_data.validated_data)
            token = Token.objects.create(user=user)
            sd = dict(ser_data.data)
            sd['token'] = str(token)
            return Response(sd, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    