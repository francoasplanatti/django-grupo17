from django.db import models
from django.core.exceptions import ValidationError


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
    patente = models.CharField(verbose_name="Patente", unique=True)
    vencimiento_vtv = models.DateField(verbose_name="Fecha de vencimiento")

    def clean_patente(self):
        patente = self.cleaned_data['patente']
        
        if not (patente[0:3].isalpha() and patente[4:6].isdigit()) or ((patente[0:2].isalpha() and patente[3:4].isdigit()) and patente[5:6].isalpha()): 
            raise ValidationError("La patente no es válida")
        return self.cleaned_data['patente']

    def __str__(self):
        return self.marca + " " + self.modelo


class Area(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    descripcion = models.CharField(max_length=150, null=True, verbose_name="Descripcion del área") 
    jefe = models.ForeignKey(Jefe, on_delete=models.CASCADE, related_name="areas")
    bomberos = models.ManyToManyField(Bombero, through="Alta", related_name="areas")

    def __str__(self):
        return self.nombre


class Alta(models.Model):
    bombero = models.ForeignKey(Bombero, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha de alta")

    def __str__(self):
        return f"{self.bombero.nombre_completo()} - {self.area.nombre}"