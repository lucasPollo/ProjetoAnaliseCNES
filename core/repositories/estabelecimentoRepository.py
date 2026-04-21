from django.db import connections


class EstabelecimentoRepository:

    @staticmethod
    def retornar_resumo(cnes):
        with connections['cnes'].cursor() as cursor:

            cursor.execute("""
                SELECT 
                    e.cnes,
                    e.nomefantasia,
                    e.idmunicipio,
                    COUNT(pv.idprofissional) AS total_profissionais
                FROM estabelecimentos e
                LEFT JOIN profissionaisvinculosnosestabelecimentos pv
                    ON pv.idestabelecimento = e.idestabelecimento
                WHERE e.cnes = %s
                GROUP BY e.cnes, e.nomefantasia, e.idmunicipio
            """, [cnes])

            return cursor.fetchone()