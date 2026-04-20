from django.http import JsonResponse
from core.services.indicadoresService import IndicadoresService


def distribuicao_cbo(request):
    municipio = request.GET.get('municipio')

    if not municipio:
        return JsonResponse({"error": "parametro de municipio obrigatorio"}, status=400)

    data = IndicadoresService.distribuicao_cbo(municipio)

    return JsonResponse(data, safe=False)