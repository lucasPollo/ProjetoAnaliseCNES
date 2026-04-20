from core.repositories.analiseRepository import AnaliseRepository


class AnaliseService:

    @staticmethod
    def profissionais_sobrecarga():
        resultados = AnaliseRepository.profissionais_sobrecarga()

        return [
            {
                "cns": r[0],
                "carga_total": r[1]
            }
            for r in resultados
        ]