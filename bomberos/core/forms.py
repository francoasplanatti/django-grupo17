from django import forms
from django.core.exceptions import ValidationError
from .models import Jefe, Bombero, Vehiculo


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


class VehiculosModelForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
    
    def clean_patente(self):
        patente = self.cleaned_data.get('patente', '').strip()

        if len(str(patente)) > 7 or len(str(patente)) < 6: 
            raise ValidationError("La patente no es válida")
        
        if not (patente[0:3].isalpha() and patente[4:6].isdigit()) or ((patente[0:2].isalpha() and patente[3:4].isdigit()) and patente[5:6].isalpha()): 
            raise ValidationError("La patente no es válida")
        
        return patente
    

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