from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Branch
from .serializers import *
from permissions import *

from content.models import Content
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser


class BranchCreateAPI(APIView):
    permission_classes = (CustomPerm,)
    # permission_classes = [AllowAny,]
    # serializer_class = BranchSerializer
    # @csrf_exempt
    def post(self, request):
        ser_data = BranchSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data, request.user)
            
            return Response({"response": "success"}, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

