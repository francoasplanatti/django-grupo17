from django.shortcuts import render

def index(request):
    return render(request, "core/index.html")

def personal(request):
    return render(request, "core/personal.html")

def personal_historico(request, year):
    listado = [
        ['Tom Cruise', 'Jefe de área'],
        ['Leo DiCaprio', 'Bombero'],
        ['Will Smith', 'Bombero'],
        ['Vin Diesel', 'Bombero'],
        ['Ryan Gosling', 'Bombero']
    ]

    context = {
        'año': year,
        'listado_historico': listado,
        'cant_personal': len(listado),
    }

    return render(request, "core/personal_historico.html", context)

def vehiculos(request):
    return render(request, "core/vehiculos.html")