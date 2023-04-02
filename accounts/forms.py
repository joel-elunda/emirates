from django import forms
from accounts.models import Profile
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ('email', 'password')

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'gender', 'phone', 'bio', 'photo', 'address')
        
        
class UpdateProfileForm(forms.ModelForm):  
    class Meta: 
        model = Profile  
        fields = ('phone', 'gender', 'bio', 'photo', 'address')
        
        GENDER_CHOICES = (
            ('F', 'Féminin'),
            ('M', 'Masculin'),
        ) 
        
        widgets = {
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Numéro de téléphone'
            }),
            
            'gender': forms.Select( 
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Genre', }, choices=GENDER_CHOICES),
                    
            'address': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Entrer votre adresse physique'
            }),
             
            
            'bio' : forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Entrer votre bio'
            }), 
        }