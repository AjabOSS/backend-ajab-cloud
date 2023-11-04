from django.db import models

class Content(models.Model):
    data = models.FileField(upload_to="contents/", null=True, blank=True)
    branch = models.ForeignKey("branch.Branch", related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return "1"