from django.shortcuts import render

def index(request):
    return render(request, "core/index.html")

def personal(request):
    return render(request, "core/personal.html")

def vehiculos(request):
    return render(request, "core/vehiculos.html")