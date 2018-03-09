from django.shortcuts import render
from django.http import HttpResponse
from .form import RegisterForm,SignInViaEmailForm
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

class SignIn(FormView):
    template_name = 'members/login.html'
    form_class = SignInViaEmailForm
    success_url = 'index'
    def form_valid(self,form):
        return super().form_valid(form)

    