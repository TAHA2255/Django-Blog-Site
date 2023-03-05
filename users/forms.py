from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import profile

class userregisterform(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class user_update(forms.ModelForm):
    #email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']
        
class profile_update(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']



