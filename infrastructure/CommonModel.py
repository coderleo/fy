from django.db import models
class CommonModel(models.Model):
    created_time = models.DateTimeField("created time when current record is created",auto_now_add=True)
    modified_time = models.DateTimeField("modified time when current record is modified",auto_now=True)
    class Meta:
        abstract = True

