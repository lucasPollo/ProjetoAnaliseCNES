class Indicador:
    def __init__(self, municipio, cbo, nome_cbo, total):
        self.municipio = municipio
        self.cbo = cbo
        self.nome_cbo = nome_cbo
        self.total = total
        
        def __str__(self):
         return f"Indicador(municipio='{self.municipio}', cbo='{self.cbo}', nome_cbo='{self.nome_cbo}', total={self.total})"