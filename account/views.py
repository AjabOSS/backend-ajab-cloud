from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken

from myuser.models import EmailConfirmationToken
from .serializers import *


class UserRegisterAPI(APIView):
    permission_classes = [AllowAny,]
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.data)
        if ser_data.is_valid():
            user = ser_data.create(ser_data.validated_data)
            token = Token.objects.create(user=user)
            EmailConfirmationToken.objects.create(user=user)
            sd = dict(ser_data.data)
            sd['token'] = str(token)
            return Response(sd, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)



class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = CustomAuthTokenSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'is_email_verified': user.is_email_verified
        })