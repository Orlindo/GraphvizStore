import array

class Peca:

    def __init__(self, nome):
        self.nome = nome
        self.filhos = []
        self.pais = []
        self.qtd_filhos = []
        self.qtd_pais = []

    def toString(self):
        return self.nome