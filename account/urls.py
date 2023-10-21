from django.urls import path

from .views import *



urlpatterns = [
    path("register/", UserRegisterAPI.as_view()),
    path("api-token-auth/", CustomAuthToken.as_view()),
    path("verify-email/", EmailCodeVerificationAPI.as_view()),
    path("send-verification-email/", SendVerificationEmailAPI.as_view()),
]
