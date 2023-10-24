from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.db import IntegrityError
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import CreateForm, VehiculosForm
from .models import Bombero, Jefe, Vehiculo

def index(request):
    return render(request, "core/index.html")

def personal(request):
    return render(request, "core/personal.html")

def personal_form(request):
    if request.method == "POST":
        formulario = CreateForm(request.POST)
        if formulario.is_valid():
            messages.info(request, "Personal dado de alta correctamente")
            return redirect(reverse("personal"))
    else:
        formulario = CreateForm()

    context = {
        'create_form': formulario
    }

    return render(request, "core/personal_form.html", context)

def personal_historico(request, year):

    listado = Bombero.objects.all().order_by('dni')

    context = {
        'año': year,
        'listado_historico': listado,
        'cant_personal': len(listado),
    }

    return render(request, "core/personal_historico.html", context)

def vehiculos(request):
    return render(request, "core/vehiculos.html")

def vehiculos_form(request):
    context = {}

    if request.method == "POST":
        vehiculos_form = VehiculosForm(request.POST)

        if vehiculos_form.is_valid():
            nuevo_vehiculo = Vehiculo(
                marca = vehiculos_form.cleaned_data['marca'],
                modelo = vehiculos_form.cleaned_data['modelo'],
                patente = vehiculos_form.cleaned_data['patente'],
                vencimiento_vtv = vehiculos_form.cleaned_data['vencimiento_vtv'],
            )

            try:
                nuevo_vehiculo.save()

            except IntegrityError as ie:
                messages.error(request, "Ocurrió un error al intentar registrar el vehículo")
                return redirect(reverse("index"))

            messages.info(request, "Vehículo registrado correctamente")
            return redirect(reverse("vehiculos"))
    else:
        vehiculos_form = VehiculosForm()

    context['vehiculos_form'] = VehiculosForm

    return render(request, 'core/vehiculos_form.html', context)


class JefeCreateView(CreateView):
    model = Jefe
    template_name = 'core/jefes_form.html'
    success_url = 'historico'
    fields = '__all__'


class JefeListView(ListView):
    model = Jefe
    context_object_name = 'jefes_historico'
    template_name = 'core/jefes_historico.html'
    ordering = ['cuit']