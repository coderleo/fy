from django.shortcuts import render
from django.http import HttpResponse
from .form import RegisterForm,SignInForm
from .models import Member
from django.views.generic.edit import FormView
# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
          
            m = form.save(commit=False)
            m.set_password(form.cleaned_data['password1'])
            m.save()      
    else:
       
        form = RegisterForm()
    
    return render(request,'members/register.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        print(Member.check_password('aa','bb'))
        # form.cleaned_data
    else:
        form = SignInForm()
    return render(request,'members/login.html',{'form':form})


   

    