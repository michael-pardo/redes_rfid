from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource
from import_export.fields import Field

from core.models import Usuario, Tarjeta, Lector, Registro


@admin.register(Usuario)
class UsuarioModelAdmin(ImportExportModelAdmin):
    list_display = ['user', 'get_name', 'documento']
    list_display_links = ['user', 'get_name', 'documento']
    search_fields = ['user__first_name', 'user__last_name', 'user__username',
                     'documento'
                     ]
    raw_id_fields = ['user']
    readonly_fields = [
        'fecha_creacion', 'fecha_actualizacion', 'creado_por',
        'actualizado_por'
    ]

    def get_name(self, obj):
        return obj.user.get_full_name()

    get_name.short_description = 'nombre'


@admin.register(Tarjeta)
class TarjetaModelAdmin(ImportExportModelAdmin):
    list_display = ['usuario', 'codigo', 'tipo']
    list_display_links = ['usuario', 'codigo', 'tipo']
    search_fields = ['usuario__user__first_name', 'usuario__user__last_name',
                     'usuario__user__username', 'usuario__documento', 'codigo']
    raw_id_fields = ['usuario']
    readonly_fields = [
        'fecha_creacion', 'fecha_actualizacion', 'creado_por',
        'actualizado_por'
    ]
    list_filter = ['tipo', 'usuario']


@admin.register(Lector)
class LectorModelAdmin(ImportExportModelAdmin):
    list_display = ['codigo', 'ubicacion']
    list_display_links = ['codigo', 'ubicacion']
    readonly_fields = [
        'fecha_creacion', 'fecha_actualizacion', 'creado_por',
        'actualizado_por'
    ]


class RegistroResource(ModelResource):
    nombre = Field()
    usuario = Field()
    documento = Field()
    ubicacion = Field(attribute='lector__ubicacion', column_name='ubicacion')

    class Meta:
        model = Registro
        fields = ['isbn', 'usuario', 'nombre', 'documento', 'ubicacion',
                  'fecha']
        export_order = ['usuario', 'nombre', 'documento', 'ubicacion',
            'fecha'
        ]

    def dehydrate_nombre(self, registro):
        return '{} {}'.format(registro.tarjeta.usuario.user.first_name,
                              registro.tarjeta.usuario.user.last_name)

    def dehydrate_usuario(self, registro):
        return '{}'.format(registro.tarjeta.usuario.user.username)

    def dehydrate_documento(self, registro):
        return '{}'.format(registro.tarjeta.usuario.documento)


@admin.register(Registro)
class RegistroModelAdmin(ImportExportModelAdmin):
    resource_class = RegistroResource
    list_display = ['tarjeta', 'lector', 'fecha']
    list_display_links = ['tarjeta', 'lector', 'fecha']
    raw_id_fields = ['tarjeta', 'lector']
    list_filter = ['tarjeta', 'lector']
    search_fields = ['tarjeta__codigo', 'tarjeta__usuario__documento',
                     'tarjeta__usuario__user__username',
                     'tarjeta__usuario__user__first_name',
                     'tarjeta__usuario__user__last_name',
                     'lector__codigo'
                     ]
    readonly_fields = ['fecha']
