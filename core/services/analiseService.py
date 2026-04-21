from core.repositories.analiseRepository import AnaliseRepository


class AnaliseService:

    @staticmethod
    def profissionais_sobrecarga():
        resultados = AnaliseRepository.profissionais_sobrecarga()

        return [
            {
                "id_profissional": resultado["idprofissional"],
                "carga_total": resultado["carga_total"]
            }
            for resultado in resultados
        ]