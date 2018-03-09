from django.urls import path
from . import views 

app_name = 'members'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('',views.index,name='index'),
    path('sigin/',views.SignIn.as_view(),name='sigin')
]