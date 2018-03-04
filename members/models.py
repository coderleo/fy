from django.db import models
from infrastructure import CommonModel
class Member(CommonModel.CommonModel):
    name = models.CharField(max_length=100,null=False)
    phone_number = models.CharField(max_length=20,null=False)
    nick_name = models.CharField(max_length=100,null=False)
    email = models.EmailField(null =False)
    birthday = models.DateField()
    gender_choices = (
        (0,'Secret'),
        (1,'Male'),
        (2,'Female')

    )
    gender = models.SmallIntegerField(choices=gender_choices,default=0)
    password = models.CharField(max_length=200,null=False,default='')
class LoginLog(CommonModel.CommonModel):
    member = models.ForeignKey(Member,on_delete=models.CASCADE
    ,db_index=False)
    login_ip = models.GenericIPAddressField()