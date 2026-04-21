
from core.repositories.indicadoresRepository import IndicadoresRepository
class IndicadoresService:

    @staticmethod
    def distribuicao_cbo(municipio):
        resultados = IndicadoresRepository.distribuicao_cbo(municipio)

        return [
            {
                "municipio": r[0],
                "cbo": r[1],
                "total": r[2]
            }
            for r in resultados
        ]