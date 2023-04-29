from django.contrib import admin
from django.urls import path, include
from . import views

app_name='App_Login'

urlpatterns = [
    path('signup/',views.sign_up,name='signup'),
    
]
