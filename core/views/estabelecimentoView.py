from django.http import JsonResponse
from core.services.estabelecimentoService import EstabelecimentoService


def resumo_estabelecimento(request, cnes):
    data = EstabelecimentoService.retornar_resumo(cnes)

    if not data:
        return JsonResponse(
            {'erro': 'informe um codigo cnes valido'},
            status=404
        )

    return JsonResponse(data)