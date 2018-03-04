from django import forms
from .models import Member
import datetime
class RegisterForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.SelectDateWidget(
        years=range(1955,datetime.datetime.now().year)))
    confirm_password = forms.CharField(widget=forms.PasswordInput())
  
    class Meta:
        model =Member
        fields = ['name','phone_number','nick_name','gender','birthday','password','email']
        widgets = {
            'password':forms.PasswordInput(),
            'gender':forms.RadioSelect()
        }
    def clean(self):
        cleaned_data = super(RegisterForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('password and confirm_password does not match')