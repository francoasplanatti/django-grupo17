from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    email = models.EmailField(max_length=150, verbose_name="Email")
    dni = models.IntegerField(verbose_name="DNI", unique=True)
    area = models.CharField(max_length=100, verbose_name="Area", null=True)

    def clean_dni(self):
        if not (0 < self.cleaned_data['dni'] <= 99999999):
            raise ValidationError("El DNI debe ser un numero positivo de 8 digitos")
        return self.cleaned_data['dni']

    class Meta:
        abstract = True

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    
    def __str__(self):
        return self.nombre_completo()
    
class Bombero(Persona):
    numero_placa = models.CharField(max_length=100, verbose_name="Numero de placa")
    rol = models.CharField(max_length=50, verbose_name="Rol", null=True)


class Jefe(Persona):
    cuit = models.CharField(max_length=100, verbose_name="Cuit")


class Vehiculo(models.Model):
    marca = models.CharField(max_length=100, verbose_name="Marca")
    modelo = models.CharField(max_length=100, verbose_name="Modelo")
    patente = models.CharField(max_length=100, verbose_name="Patente")
    vencimiento_vtv = models.DateField(verbose_name="Fecha de vencimiento")


class Area(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    descripcion = models.CharField(max_length=150, null=True, verbose_name="Descripcion del área") 
    jefe = models.ForeignKey(Jefe, on_delete=models.CASCADE, related_name="+")
    bomberos = models.ManyToManyField(Bombero, through="Alta", related_name="+")


class Alta(models.Model):
    bombero = models.ForeignKey(Bombero, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha de alta")