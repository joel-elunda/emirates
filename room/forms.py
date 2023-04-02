from django import forms
from room.models import RoomModel

class RoomModelForm(forms.ModelForm):
    
    class Meta:
        model = RoomModel
        fields = (
            'guest',
            'date_start',
            'date_end',
            'nb_child',
            'nb_adult', 
        )
        
        widgets = {
            'guest' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
                'required': True,
            }),
            'date_start' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
                'required': True,
            }),
            'date_end' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
                'required': True,
            }),
            'nb_child' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
                'required': True,
            }),
            'nb_adult'  : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
                'required': True,
            }),
        }
        
        
        
        
        
        
        
        
        
        
        
