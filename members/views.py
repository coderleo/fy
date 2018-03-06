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
          
            m = form.save(commit=False)
            m.set_password(form.cleaned_data['password1'])
            m.save()
            # print(m.name)
    else:
       
        form = RegisterForm()
    
    return render(request,'members/register.html',{'form':form})