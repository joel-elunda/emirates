from django import forms 
from plate.models import PlateModel

class PlateModelForm(forms.ModelForm):
    
    class Meta:
        model = PlateModel
        fields = ('client', 'name', 'description')

        widgets = {
             
            'client' : forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': '',
            }),
            'name' : forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': '',
            }),
            'description' : forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': '',
            }),
            
        }