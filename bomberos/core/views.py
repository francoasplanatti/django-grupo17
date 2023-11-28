from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import IntegrityError
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import VehiculosModelForm, JefesModelForm, BomberosModelForm
from .models import Bombero, Jefe, Vehiculo

def index(request):
    return render(request, "core/index.html")

@login_required
def personal(request):
    return render(request, "core/personal.html")


class BomberoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ("core.view_bombero")
    model = Bombero
    template_name = 'core/personal_form.html'
    success_url = 'historico'
    form_class = BomberosModelForm


class BomberoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ("core.view_bombero")
    model = Bombero
    context_object_name = 'personal_historico'
    template_name = 'core/personal_historico.html'
    ordering = ['area']

@login_required
def editarBombero(request, dni):
    bombero = Bombero.objects.get(dni=dni)
    form = BomberosModelForm(instance=bombero)

    if request.method == 'POST':
        form = BomberosModelForm(request.POST, instance=bombero)
        if form.is_valid():
            form.save()
            messages.info(request, "Información guardada correctamente")
            return redirect('/personal/historico')

    context = {'bombero':bombero, 'form': form}
    return render(request, 'core/personal_edit.html', context)

@login_required
def eliminarBombero(request, dni):
    bombero = Bombero.objects.get(dni=dni)
    bombero.delete()

    return redirect('/personal/historico')


@login_required
def vehiculos(request):
    return render(request, "core/vehiculos.html")


class VehiculosCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ("core.view_vehiculo")
    model = Vehiculo
    template_name = 'core/vehiculos_form.html'
    success_url = '/../vehiculos'
    form_class = VehiculosModelForm


class VehiculosListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ("core.view_vehiculo")
    model = Vehiculo
    context_object_name = 'vehiculos'
    template_name = 'core/vehiculos.html'
    ordering = ['marca']


@login_required
def editarVehiculo(request, patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    form = VehiculosModelForm(instance=vehiculo)

    if request.method == 'POST':
        form = VehiculosModelForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('/vehiculos')

    context = {'vehiculo':vehiculo, 'form': form}
    return render(request, 'core/vehiculos_edit.html', context)

@login_required
def eliminarVehiculo(request, patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    vehiculo.delete()

    return redirect('/vehiculos')


class JefeCreateView(CreateView, PermissionRequiredMixin, LoginRequiredMixin):
    permission_required = ("core.view_jefe")
    model = Jefe
    template_name = 'core/jefes_form.html'
    success_url = 'historico'
    form_class = JefesModelForm


class JefeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ("core.view_jefe")
    model = Jefe
    context_object_name = 'jefes_historico'
    template_name = 'core/jefes_historico.html'
    ordering = ['cuit']


@login_required
def editarJefe(request, dni):
    jefe = Jefe.objects.get(dni=dni)
    form = JefesModelForm(instance=jefe)

    if request.method == 'POST':
        form = JefesModelForm(request.POST, instance=jefe)
        if form.is_valid():
            form.save()
            return redirect('/jefes/historico')

    context = {'jefe':jefe, 'form': form}
    return render(request, 'core/jefes_edit.html', context)

@login_required
def eliminarJefe(request, dni):
    jefe = Jefe.objects.get(dni=dni)
    jefe.delete()

    return redirect('/jefes/historico')


def contacto(request):
    return render(request, "core/contacto.html")
