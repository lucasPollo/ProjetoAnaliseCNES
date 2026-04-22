from django.http import JsonResponse
from core.services.analiseService import AnaliseService


def sobrecarga(request):
    dadosService = AnaliseService.profissionais_sobrecarga()
    
    if not dadosService:
        return JsonResponse(
            {'erro': 'nenhum profissiona encontrado'},
            status=404
        )
    return JsonResponse(dadosService, safe=False)