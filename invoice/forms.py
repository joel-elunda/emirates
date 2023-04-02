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
                'placeholder': ''
            }),
            'user': forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': ''
            }),
            'plate': forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': ''
            }),
            'room': forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': ''
            }),
            
        }