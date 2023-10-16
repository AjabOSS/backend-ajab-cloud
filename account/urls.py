from django.urls import path

from .views import *

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("register/", UserRegisterAPI.as_view()),
    path("api-token-auth/", obtain_auth_token),
]
