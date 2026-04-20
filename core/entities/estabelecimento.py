class Estabelecimento:
    def __init__(self, cnes, nome, municipio, total_profissionais):
        self.cnes_id = cnes
        self.nome = nome
        self.municipio = municipio
        self.total_profissionais = total_profissionais

    def __str__(self):
        return f"Estabelecimento(cnes_id={self.cnes_id}, nome='{self.nome}', municipio='{self.municipio}', total_profissionais={self.total_profissionais})"