from django import forms

class RegisterForm(forms.Form):
    '''
    sudo add-apt-repository ppa:fcitx-team/nightly
    '''
    name = forms.CharField(label='name',max_length=100)
    nick_name = forms.CharField(label='nick name',max_length=100)
    phone_number = forms.CharField(label='phone number',max_length=20)