from django import forms
from .models import Member
import datetime
from django.utils.translation import gettext_lazy as _
class RegisterForm(forms.ModelForm):
    field_order = ['nick_name','name','phone_number','email','password1',
    'password2','gender','birthday']
    
    password1 = forms.CharField(label=_('password'),widget=forms.PasswordInput())
    password2 = forms.CharField(label=_('password confirmation'),
    widget=forms.PasswordInput,
    help_text=_("Enter the same password as above, for verification"))
    birthday = forms.DateField(widget=forms.SelectDateWidget(
        years=range(1955,datetime.datetime.now().year)))
    class Meta:
        model =Member
        fields = ['name','phone_number','nick_name','gender','birthday','email']
        widgets = {
           
            'gender':forms.RadioSelect()
        }
    def clean(self):
        cleaned_data = super(RegisterForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('password and confirm_password does not match')