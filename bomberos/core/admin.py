from django.contrib import admin
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.admin import UserAdmin
from core.models import Bombero, Jefe, Vehiculo, Area, Alta
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django import forms

class SGIBAdminSite(admin.AdminSite):
    site_header = "Sistema de Gestión Integral de Bomberos"
    site_title = "SGIB - Admin"
    index_title = ""
    empty_value_display = "vacio"

admin_site = SGIBAdminSite(name='admin')

User = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()

        if not is_superuser:
            disabled_fields |= {
                'username',
                'is_superuser',
                'user_permissions',
            }

        if (
            not is_superuser
            and obj is not None
            and obj == request.user
        ):
            disabled_fields |= {
                'is_staff',
                'is_superuser',
                'user_permissions',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            fieldsets = list(fieldsets)
            for fieldset in fieldsets:
                fieldset[1]['fields'] = [f for f in fieldset[1]['fields'] if f not in ('groups', 'user_permissions')]

        return fieldsets
    
    def get_inline_instances(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_inline_instances(request, obj)
        else:
            return []

class AreasInline(admin.TabularInline):
    model = Area.bomberos.through

class BomberosInline(admin.TabularInline):
    model = Area.bomberos.through
    extra = 1

class BomberoAdmin(admin.ModelAdmin):
    list_display = ( 'numero_placa', 'nombre', 'apellido', 'dni', 'area', 'rol')
    list_editable = ('apellido', 'nombre')
    list_display_links = ['numero_placa']
    search_fields = ['apellido']
    inlines = [AreasInline]

class AreaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    inlines = [BomberosInline]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'bomberos':
            kwargs["queryset"] = Bombero.objects.filter().order_by("apellido")

        return super().formfield_for_manytomany(db_field, request, **kwargs)
    
class AltaAdmin(admin.ModelAdmin):
    list_display = ('bombero', 'area', 'fecha')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.bombero.area = obj.area
        obj.bombero.save()


admin_site.register(Bombero, BomberoAdmin)
admin_site.register(Jefe)
admin_site.register(Vehiculo)
admin_site.register(Area, AreaAdmin)
admin_site.register(Alta, AltaAdmin)
admin_site.register(User, CustomUserAdmin)
admin_site.register(Group)
admin_site.register(Permission)
