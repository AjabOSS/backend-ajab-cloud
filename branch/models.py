from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

class Branch(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    contents = models.ManyToManyField("content.Content", related_name="content")#!
    
    up_voted_uesrs = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="up_voted_uesr", blank=True)
    down_voted_uesrs = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="down_voted_uesr", blank=True)
    
    date = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='author')
