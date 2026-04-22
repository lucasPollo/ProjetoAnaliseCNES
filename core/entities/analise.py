class Analise:
    def __init__(self, id_profissional, carga_total):
        self.id_profissional = id_profissional
        self.carga_total = carga_total
        
        def __str__(self):
         return f"AnalisesSobrecarga(id_profissional='{self.id_profissional}', carga_total={self.carga_total})"