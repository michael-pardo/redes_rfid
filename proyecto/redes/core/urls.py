from django.urls import path

from core.views import agregar_registro

app_name = 'core'
urlpatterns = [
    path(
        route='registro/',
        view=agregar_registro,
        name='agregar_registro'
    )
]
