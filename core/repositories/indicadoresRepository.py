from django.db import connections


class IndicadoresRepository:

    @staticmethod
    def distribuicao_cbo(municipio):
        with connections['cnes'].cursor() as cursor:

            cursor.execute("""
                SELECT 
                    m.nomemunicipio AS municipio,
                    pv.idespecialidade AS cbo,
                    esp.nomedaespecialidade AS nome_cbo,
                    COUNT(*) AS total
                FROM profissionaisvinculosnosestabelecimentos pv

                JOIN estabelecimentos e
                    ON pv.idestabelecimento = e.idestabelecimento

                JOIN municipios m
                    ON e.idmunicipio = m.idmunicipio

                LEFT JOIN especialidades esp
                    ON pv.idespecialidade = esp.idespecialidade

                WHERE e.idmunicipio = %s

                GROUP BY 
                    m.nomemunicipio, 
                    pv.idespecialidade, 
                    esp.nomedaespecialidade
                ORDER BY total DESC
            """, [municipio])



            return cursor.fetchall()