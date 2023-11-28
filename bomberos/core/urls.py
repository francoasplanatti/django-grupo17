from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),

        # Sessions
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

        # Personal
    path('personal', views.personal, name='personal'),
    path('personal/form', views.BomberoCreateView.as_view(), name='personal_form'),
    path('personal/historico', views.BomberoListView.as_view(), name="personal_historico"),
    path('editarBombero/<dni>', views.editarBombero, name="editarBombero"),
    path('eliminarBombero/<dni>', views.eliminarBombero, name="eliminarBombero"),

        # Jefes
    path('jefes/form', views.JefeCreateView.as_view(), name="jefes_form"),
    path('jefes/historico', views.JefeListView.as_view(), name="jefes_historico"),
    path('editarJefe/<dni>', views.editarJefe, name="editarJefe"),
    path('eliminarJefe/<dni>', views.eliminarJefe, name="eliminarJefe"),

        # Vehículos
    path('vehiculos', views.VehiculosListView.as_view(), name='vehiculos'),
    path('vehiculos/form', views.VehiculosCreateView.as_view(), name="vehiculos_form"),
    path('editarVehiculo/<patente>', views.editarVehiculo, name="editarVehiculo"),
    path('eliminarVehiculo/<patente>', views.eliminarVehiculo, name="eliminarVehiculo"),

        # Contacto
    path('contacto', views.contacto, name='contacto'),
]