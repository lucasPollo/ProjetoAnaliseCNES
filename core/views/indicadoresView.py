from django.http import JsonResponse
from core.services.indicadoresService import IndicadoresService


def distribuicao_cbo(request):
    municipio = request.GET.get('municipio')
    print(municipio)

    if not municipio:
        return JsonResponse({"erro": "obrigatorio passar um municipio id"}, status=400)

    data = IndicadoresService.distribuicao_cbo(municipio)

    return JsonResponse(data, safe=False)