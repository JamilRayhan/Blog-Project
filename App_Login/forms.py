from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email= forms.EmailField(label="Email Address",  required=True)
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')
        
        
class UserProfileChange(UserChangeForm):
    class Meta:
        model=User
        fields= ('username','email','first_name','last_name')