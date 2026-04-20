class IndicadoresRepository:

    @staticmethod
    def distribuicao_cbo(municipio):
        from django.db import connections

        with connections['cnes'].cursor() as cursor:

            cursor.execute("""
                SELECT 
                    pv.idespecialidade AS cbo,
                    COUNT(*) as total
                FROM profissionaisvinculosnosestabelecimentos pv
                JOIN estabelecimentos e
                    ON pv.idestabelecimento LIKE (e.cnes::text || '%')
                WHERE e.idmunicipio = %s
                GROUP BY pv.idespecialidade
                ORDER BY total DESC
            """, [municipio])

            return cursor.fetchall()