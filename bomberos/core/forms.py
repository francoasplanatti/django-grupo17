from django import forms
from django.core.exceptions import ValidationError
from .models import Jefe


class CreateForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre", 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form_nombre'})
        )
    apellido = forms.CharField(
        label="Apellido", 
        required=True
        )
    dni = forms.IntegerField(
        label="DNI", 
        required=True
        )
    mail = forms.EmailField(
        label="Mail", 
        required=True
        )
    rol = forms.CharField(
        label="Rol", 
        required=True
        )
    fecha_alta = forms.DateField(
        label="Fecha de alta", 
        required=True
        )
    
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
    patente = forms.IntegerField(
        label="Patente", 
        required=True
        )
    vencimiento_vtv = forms.DateField(
        label="Vencimiento del VTV", 
        required=True
        )
    

class JefesModelForm(forms.ModelForm):
    class Meta:
        model = Jefe
        fields = '__all__'

    def clean_cuit(self):
        cuit = self.cuit.strip()

        if not cuit.isdigit():
            raise ValidationError("El CUIT debe contener solo dígitos.")

        if len(cuit) != 11:
            raise ValidationError("El CUIT debe tener 11 dígitos.")
        
        self.changed_data['cuit'] = cuit
        return self.changed_data['cuit']