from django.db import connections


class EstabelecimentoRepository:

    @staticmethod
    def retornar_resumo(cnes):
        with connections['cnes'].cursor() as cursor:

            cursor.execute("""
                SELECT 
                    e.cnes,
                    e.nomefantasia,
                    e.idmunicipio
                FROM estabelecimentos e
                WHERE e.cnes = %s
            """, [cnes])

            estabelecimento = cursor.fetchone()

            if not estabelecimento:
                return None

            cursor.execute("""
                SELECT COUNT(*)
                FROM profissionaisvinculosnosestabelecimentos
            """)

            total = cursor.fetchone()[0]

            return (
                estabelecimento[0],
                estabelecimento[1],
                estabelecimento[2],
                total
            )