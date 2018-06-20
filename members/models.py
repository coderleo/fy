from django.db import models
from infrastructure import CommonModel
from django.contrib.auth import hashers
class Member(CommonModel.CommonModel):
    def __str__(self):
        return '%s-%s-%s' %(self.name,self.nick_name,self.email)
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
    def set_password(self,password):
        self.password = hashers.make_password(password)
    @classmethod  
    def check_password(cls,email,password):
        
        m = Member.objects.filter(email=email)
        if len(m)>0:
            if hashers.check_password(password,m[0].password):
                return True
        return False
class LoginLog(CommonModel.CommonModel):
    member = models.ForeignKey(Member,on_delete=models.CASCADE
    ,db_index=False)
    login_ip = models.GenericIPAddressField()