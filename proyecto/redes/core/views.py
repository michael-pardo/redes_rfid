from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from core.models import Registro, Lector, Tarjeta


@csrf_exempt
def agregar_registro(request):
    if request.method == 'POST':
        id = request.POST.get('id', '')
        codigo_lector = request.POST.get('lector', '')

        lector = Lector.objects.filter(codigo__iexact=codigo_lector).first()
        tarjeta = Tarjeta.objects.filter(codigo__iexact=id).first()

        if tarjeta and lector:
            Registro.objects.create(
                tarjeta=tarjeta,
                lector=lector
            )
            return HttpResponse('Registro completado')
        else:
            return HttpResponseBadRequest('Lector o tarjeta no registrado id={} lector={}'.format(id,codigo_lector))
    else:
        return HttpResponseBadRequest()
