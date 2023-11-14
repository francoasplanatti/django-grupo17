from django.contrib import admin
from core.models import Bombero, Jefe, Vehiculo, Area, Alta

"""
class SGIBAdminSite(admin.AdminSite):
    site_header = "Sistema de Gestión Integral de Bomberos"
    site_title = "Administración para superusers"
    index_title = "Administración del sitio"
    empty_value_display = "vacio"


class BomberoAdmin(admin.ModelAdmin):
    list_display = ( 'numero_placa', 'nombre', 'apellido')
    list_editable = ('apellido', 'nombre')
    list_display_links = ['numero_placa']
    search_fields = ['apellido']

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('nombre')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field == 'bomberos':
            kwargs["queryset"] = Bombero.objects.filter().order_by("apellido")

        return super().formfield_for_manytomany(db_field, request, **kwargs)
"""

admin.site.register(Bombero)
admin.site.register(Jefe)
admin.site.register(Vehiculo)
admin.site.register(Area)
admin.site.register(Alta)
