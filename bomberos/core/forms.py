from django import forms
from django.core.exceptions import ValidationError
from .models import Jefe, Bombero


class BomberosModelForm(forms.ModelForm):
    class Meta:
        model = Bombero
        fields = '__all__'

    def clean_dni(self):
        if len(str(self.cleaned_data["dni"])) > 8 or len(str(self.cleaned_data["dni"])) < 7: 
            raise ValidationError("El DNI debe ser válido")
        
        return self.cleaned_data["dni"]
        
    def clean(self):
        if self.cleaned_data["nombre"] == "" and self.cleaned_data["apellido"] == "":
            raise ValidationError("El usuario ya existe")
        
        return self.cleaned_data


class VehiculosForm(forms.Form):
    marca = forms.CharField(
        label="Marca", 
        required=True,
        )
    modelo = forms.CharField(
        label="Modelo", 
        required=True
        )
    patente = forms.CharField(
        label="Patente", 
        required=True
        )
    vencimiento_vtv = forms.DateField(
        label="Vencimiento del VTV", 
        required=True
        )
    
    def clean_patente(self):
        if len(str(self.cleaned_data["patente"])) > 7 or len(str(self.cleaned_data["patente"])) < 6: 
            raise ValidationError("La patente no es válida")
        
        return self.cleaned_data["patente"]
    

class JefesModelForm(forms.ModelForm):
    class Meta:
        model = Jefe
        fields = '__all__'

    def clean_cuit(self):
        cuit = self.cleaned_data.get('cuit', '').strip()

        if not cuit.isdigit():
            raise ValidationError("El CUIT debe contener solo dígitos.")

        if len(cuit) != 11:
            raise ValidationError("El CUIT debe tener 11 dígitos.")
        
        return cuit
    
    
class ContactoForm(forms.Form):
    titulo = forms.CharField(
        label="Título", 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form_style', 'placeholder':'Inserte un título'})
        )
    mensaje = forms.CharField(
        label="Mensaje", 
        required=True,
        widget=forms.Textarea(attrs={'class': 'form_style', 'placeholder':'Inserte un mensaje'})
        )
    