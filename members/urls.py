from django.urls import path
from . import views 

app_name = 'members'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('',views.index,name='index'),
    path('login/',views.login,name='login')
]