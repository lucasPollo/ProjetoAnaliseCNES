from core.repositories.estabelecimentoRepository import EstabelecimentoRepository


class EstabelecimentoService:
    
    @staticmethod
    def retornar_resumo(cnes):
        resultado = EstabelecimentoRepository.retornarResumo(cnes)
        if resultado:
                return {
                    'cnes_id': resultado[0],
                    'nome': resultado[1],
                    'municipio': resultado[2],
                    'total_profissionais': resultado[3]
                }
        return None