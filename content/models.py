from django.db import models

class Content(models.Model):
    file = models.FileField(upload_to="contents/")