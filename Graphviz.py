from graphviz import Graph
from Peca import Peca


class Graphviz:

    def __init__(self):
        self.g = Graph('Projeto', filename='projeto.gv')

    def show(self):
        self.g.view()

    def add_node(self, peca):
        self.g.node(peca.nome)

    def add_edge(self, pai, filho):
        print (pai.nome)
        self.g.edge(pai.nome, filho.nome)