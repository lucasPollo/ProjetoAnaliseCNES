from django.db import connections


class AnaliseRepository:

    @staticmethod
    def profissionais_sobrecarga():
        with connections['cnes'].cursor() as cursor:

            cursor.execute("""
                SELECT 
                    pv.idprofissional,
                    SUM(
                        COALESCE(pv.cargahorariaambulatorial, 0) +
                        COALESCE(pv.cargahorariahospitalar, 0) +
                        COALESCE(pv.cargahorariaoutros, 0)
                    ) AS carga_total
                FROM profissionaisvinculosnosestabelecimentos pv
                GROUP BY pv.idprofissional
                HAVING SUM(
                    COALESCE(pv.cargahorariaambulatorial, 0) +
                    COALESCE(pv.cargahorariahospitalar, 0) +
                    COALESCE(pv.cargahorariaoutros, 0)
                ) > 60
                ORDER BY carga_total DESC
            """)

            return cursor.fetchall()