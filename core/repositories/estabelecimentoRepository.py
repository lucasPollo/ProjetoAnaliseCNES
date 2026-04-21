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
                    m.nomemunicipio,
                    COUNT(pv.idprofissional) AS total_profissionais
                FROM estabelecimentos e
                  LEFT JOIN municipios m
                    ON e.idmunicipio = m.idmunicipio
                LEFT JOIN profissionaisvinculosnosestabelecimentos pv
                    ON pv.idestabelecimento = e.idestabelecimento
                WHERE e.cnes = %s
                GROUP BY e.cnes, e.nomefantasia, e.idmunicipio, m.nomemunicipio
            """, [cnes])

            return cursor.fetchone()