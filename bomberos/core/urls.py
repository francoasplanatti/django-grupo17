from django.urls import path , re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculos', views.vehiculos, name='vehiculos'),
    path('personal', views.personal, name='personal'),
    re_path(r'personal/(?P<year>\d{4})/$', views.personal_historico, name='personal_historico'),
]