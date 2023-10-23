from django.urls import path

from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("register/", UserRegisterAPI.as_view()),
    path("verify-email/", EmailCodeVerificationAPI.as_view()),
    path("send-verification-email/", SendVerificationEmailAPI.as_view()),
    
    
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path("api-token-auth/", CustomAuthToken.as_view()),
    
    
]
