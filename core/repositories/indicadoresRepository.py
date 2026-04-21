class IndicadoresRepository:

    @staticmethod
    def distribuicao_cbo(municipio):
        from django.db import connections

        with connections['cnes'].cursor() as cursor:

            cursor.execute("""
                SELECT 
                    m.nome AS municipio,
                    pv.idespecialidade AS cbo,
                    COUNT(*) as total
                FROM profissionaisvinculosnosestabelecimentos pv
                JOIN estabelecimentos e
                    ON pv.idestabelecimento = e.idestabelecimento
                JOIN municipios m
                    ON e.idmunicipio = m.idmunicipio
                WHERE e.idmunicipio = %s
                GROUP BY m.nome, pv.idespecialidade
                ORDER BY total DESC
            """, [municipio])

            return cursor.fetchall()