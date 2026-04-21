
from core.repositories.indicadoresRepository import IndicadoresRepository
class IndicadoresService:

    @staticmethod
    def distribuicao_cbo(municipio):
        resultados = IndicadoresRepository.distribuicao_cbo(municipio)
        if resultados:
         return [
            {
                "municipio": r[0],
                "cbo": r[1],
                "nome_cbo": r[2],
                "total": r[3]
            }
            for r in resultados
        ]