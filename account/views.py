from django.shortcuts import render, get_object_or_404
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken

from myuser.models import EmailConfirmationToken, MyUser
from .serializers import *
from .utils import send_verification_email
import uuid 


class EditUserProfileView(APIView):
    permission_classes = [IsAuthenticated,]
    def put(self, request):
        user = request.user
        srz_data = EditUserProfileSerializer(instance=user, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

class SendVerificationEmailAPI(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        if request.user.is_email_verified == False:
            send_verification_email(request.user)
            return Response({"response": "success"}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"response": "failed email alredy verifyed"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            
            
            
class EmailCodeVerificationAPI(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        user = request.user
        code = request.data['code']
        email_verify_object = EmailConfirmationToken.objects.filter(user=request.user)
        
        if len(email_verify_object) == 1:
            # print(str(code), " ",  str(email_verify_object[0].code))
            if str(code) == str(email_verify_object[0].code):
                user_obj = MyUser.objects.get(id=user.id)
                user_obj.is_email_verified = True
                user_obj.save()
                status_code = status.HTTP_202_ACCEPTED
                response = "email verification successful"
            else:
                status_code = status.HTTP_406_NOT_ACCEPTABLE
                response = "code not valid"
                

        elif len(email_verify_object) == 0:
            response = ("no email verification detected")
        else:
            response = "internal error"
            
        return Response({
            "code":code,
            "response":response
            }, status=status_code)
    
    
class UserRegisterAPI(APIView):
    permission_classes = [AllowAny,]
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.data)
        if ser_data.is_valid():
            user = ser_data.create(ser_data.validated_data)
            token = Token.objects.create(user=user)
            sd = dict(ser_data.data)
            sd['token'] = str(token)
            return Response(sd, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)



class CustomAuthToken(ObtainAuthToken):
    permission_classes = [AllowAny,]
    def post(self, request, *args, **kwargs):
        serializer = CustomAuthTokenSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username,
            'name': user.name,
            # 'profile_image': user.profile_image,
            'is_onboarded': user.is_onboarded,
            'is_email_verified': user.is_email_verified
        })
    
