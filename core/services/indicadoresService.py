from core.repositories.indicadoresRepository import IndicadoresRepository


class IndicadoresService:

    @staticmethod
    def distribuicao_cbo(municipio):
        resultados = IndicadoresRepository.distribuicao_cbo(municipio)
        if resultados:
         return [
            {
                "municipio": resultado[0],
                "cbo": resultado[1],
                "nome_cbo": resultado[2],
                "total": resultado[3]
            }
            for resultado in resultados
        ]