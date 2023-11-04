from django.urls import path
from .views import *

urlpatterns = [
    path('create/', BranchCreateAPI.as_view()),
]
