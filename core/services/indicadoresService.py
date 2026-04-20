from core.repositories.indicadoresRepository import IndicadoresRepository


class IndicadoresService:

    @staticmethod
    def distribuicao_cbo(municipio):
        resultados = IndicadoresRepository.distribuicao_cbo(municipio)

        return [
            {
                "cbo": r[0],
                "total": r[1]
            }
            for r in resultados
        ]