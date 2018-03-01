from django.db import models
from infrastructure import CommonModel
class Member(CommonModel.CommonModel):
    name = models.CharField(max_length=100,null=False)
    phone_number = models.CharField(max_length=20,null=False)
    nick_name = models.CharField(max_length=100,null=False)
    email = models.EmailField(null =False)
    birthday = models.DateField()
    
    