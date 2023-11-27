from django import forms
import re
from .models import Contacto

class ContactoForm(forms.ModelForm):
   
    class Meta:
        model = Contacto
        fields = ["nombre"]







"""class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=30, min_length=4, required=True)
    telefono = forms.CharField(label='Teléfono', max_length=15, min_length=10, required=True)
    email = forms.EmailField(label='Correo Electrónico', max_length=254, required=True)



    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        patron_telefono = re.compile(r'^\d{10,15}$')
        
        if not patron_telefono.match(telefono):
            raise forms.ValidationError('Ingrese un número de teléfono válido.')
        
        return telefono"""