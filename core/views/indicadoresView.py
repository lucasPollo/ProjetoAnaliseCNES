from django.http import JsonResponse
from core.services.indicadoresService import IndicadoresService


def distribuicao_cbo(request):
    municipio = request.GET.get('idmunicipio')
    dadosService = IndicadoresService.distribuicao_cbo(municipio)
    print(municipio)

    if not municipio:
        return JsonResponse({"erro": "obrigatorio passar um municipio id"}, status=400)


    return JsonResponse(dadosService, safe=False)