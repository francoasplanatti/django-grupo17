from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import IntegrityError
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import VehiculosForm, ContactoForm, JefesModelForm, BomberosModelForm
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
    fields = '__all__'


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

@login_required
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


class JefeCreateView(CreateView, PermissionRequiredMixin, LoginRequiredMixin):
    permission_required = ("core.view_jefe")
    model = Jefe
    template_name = 'core/jefes_form.html'
    success_url = 'historico'
    fields = '__all__'


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
    if request.method == "POST":
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            messages.info(request, "Mensaje Enviado Correctamente")
            return redirect(reverse("index"))
    else:
        formulario = ContactoForm()

    context = {
        'create_form': formulario
    }

    return render(request, "core/contacto.html", context)
