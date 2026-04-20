from django.http import JsonResponse
from core.services.analiseService import AnaliseService


def sobrecarga(request):
    data = AnaliseService.profissionais_sobrecarga()
    return JsonResponse(data, safe=False)