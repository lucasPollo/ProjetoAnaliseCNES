from django.db import connections

class EstabelecimentoRepository:
    
    
    @staticmethod
    def retornar_resumo(cnes):
        with connections['cnes'].cursor() as cursor:
           cursor.execute("""
                SELECT 
                    e.cnes,
                    e.nomefantasia,
                    e.codigomunicipio,
                    COUNT(pv.id) as total_profissionais
                FROM estabelecimentos e
                LEFT JOIN profissionaisvinculosnosestabelecimentos pv
                    ON pv.cnes = e.cnes
                WHERE e.cnes = %s
                GROUP BY e.cnes, e.nomefantasia, e.codigomunicipio
            """, [cnes])

           return cursor.fetchone()
   