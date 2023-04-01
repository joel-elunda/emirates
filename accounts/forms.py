from dataclasses import fields
from django import forms
from django.forms import  ModelForm
from django.contrib.auth.models import User 
from accounts.models import Profile

class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ('email', 'password')

class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'gender', 'phone', 'bio', 'photo', 'address')
        