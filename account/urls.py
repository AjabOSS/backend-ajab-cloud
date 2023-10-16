from django.urls import path
from .views import *


urlpatterns = [
    path("register/", UserRegisterAPI.as_view())
]
