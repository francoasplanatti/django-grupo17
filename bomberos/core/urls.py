from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('vehiculos', views.vehiculos, name='vehiculos'),
    path('vehiculos/form', views.vehiculos_form, name="vehiculos_form"),
    path('personal', views.personal, name='personal'),
    path('personal/form', views.personal_form, name='personal_form'),
    re_path(r'personal/(?P<year>\d{4})/$', views.personal_historico, name='personal_historico'),
    path('jefes/form', views.JefeCreateView.as_view(), name="jefes_form"),
    path('jefes/historico', views.JefeListView.as_view(), name="jefes_historico"),
]