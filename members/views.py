from django.shortcuts import render
from django.http import HttpResponse
from .form import RegisterForm
from .models import Member
# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            print(request.POST)
            member = Member()
            member.phone_number = form.phone_number
            member.name = form.name
            member.nick_name = form.nick_name
            member.save()
    else:
        form = RegisterForm()
    
    return render(request,'members/register.html',{'form':form})