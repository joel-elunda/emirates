from django import forms 
from invoice.models import InvoiceModel

class InvoiceModelForm(forms.ModelForm):
    
    class Meta:
        model = InvoiceModel
        fields = (
            'client',
            'user',
            'plate',
            'room', 
        )

        widgets = {
            'client': forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Nom du client'
            }), 
            'plate': forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Nom du plat'
            }),
            'room': forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Nom de la chambre'
            }),
            
        }