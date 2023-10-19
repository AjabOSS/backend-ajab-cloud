from django.contrib import admin
from .models import MyUser, EmailConfirmationToken
admin.site.register(MyUser)
admin.site.register(EmailConfirmationToken)