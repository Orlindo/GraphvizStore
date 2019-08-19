from Peca import Peca
from Graphviz import Graphviz

print("Contrutor de Conjuntos -> Peças")

def criar_peca(nome):
    peca = Peca(nome)
    print( peca.toString() + " foi criado")
    return peca #O QUE O USUARIO ENTROU

def criando_pecas():
    pecas = []

    print("Digite 0 para sair: ")
    has_next = True
    while (has_next):
        pecaUser = input("Digite o nome da Peça: ")
        if (pecaUser == '0'):
            has_next = False
        else:
            pecas.append(criar_peca(pecaUser))

    return pecas

def controla_relacionamento():
    print("RELACIONAMENTOS S2")
 
def desenhaGraph(pecas):
    graph = Graphviz()

    for p in pecas:
        graph.add_node(p)

    graph.add_edge(pecas[0], pecas[1])

    graph.show()


pecas = criando_pecas()
controla_relacionamento()

desenhaGraph(pecas)

