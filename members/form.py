from django import forms
from .models import Member
import datetime
from django.utils.translation import gettext_lazy as _
from .models import Member
class RegisterForm(forms.ModelForm):
    field_order = ['nick_name','name','phone_number','email','password1',
    'password2','gender','birthday']
    
    password1 = forms.CharField(label=_('password'),widget=forms.PasswordInput())
    password2 = forms.CharField(label=_('password confirmation'),
    widget=forms.PasswordInput,
    help_text=_("Enter the same password as above, for verification"))
    birthday = forms.DateField(widget=forms.SelectDateWidget(
        years=range(1955,datetime.datetime.now().year)))
    error_messages = {
        'unique_email':_('you can not use this email')
    }
    class Meta:
        model =Member
        fields = ['name','phone_number','nick_name','gender','birthday','email']
        widgets = {
           
            'gender':forms.RadioSelect()
        }
    def clean(self):
        cleaned_data = super(RegisterForm,self).clean()
        password = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('password2')
        if password != confirm_password:
            raise forms.ValidationError('password and confirm_password does not match')
        email = cleaned_data.get('email','')
        member_count = Member.objects.filter(email=email).count()
        if member_count>0:
            raise forms.ValidationError(self.error_messages['unique_email'])
            self.add_error('email',self.error_messages['unique_email'])    
    # def clean_email(self):
    #     email = self.cleaned_data.get('email','')
    #     member_count = Member.objects.filter(email=email).count()
    #     if member_count>0:
    #         self.add_error('email',self.error_messages['unique_email'])
    #     return self.cleaned_data

class SignInForm(forms.Form):
    email = forms.EmailField(
        label = _('Email')
    )
    password = forms.CharField(
        label = _('Password'),
        strip = False,
        widget = forms.PasswordInput,
    )
# class SignInViaEmailForm(SignIn):
#     field_order = ['email','password']
#     email = forms.EmailField(
#         label = _('Email'),
#         widget = forms.EmailInput(attrs={'placeholder':'@','autofocus':True})
#     )

#     error_messages = {
#         'invalid_login':_('Please enter a correct email and password')
#     }
#     def clean(self):
#         cleaned_data = super(SignInViaEmailForm,self).clean()
#         email = cleaned_data.get('email','').lower()
#         password = cleaned_data.get('password','')
#         member = Member.objects.filter(email=email).first()
#         if member:
#             pass
#         else:
#             self.add_error('email',self.error_messages['invalid_login'])