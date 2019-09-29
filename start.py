from Peca import Peca
from Graphviz import Graphviz

estado = 100
opcao = False

pasta = 'C:/Users/OW/GraphvizStore'

def menu():

    print("--- Bem-vindo ao GraphvizStore ----\n")
    print("Menu de opções")
    print("1 - Adicionar peças")
    print("2 - Criar relacionamentos")
    print("3 - Consultar peças")
    print("4 - Consultar relacionamentos")
    print("5 - Excluir peça")
    print("6 - Editar peças")
    print("7 - Editar Relacionamentos")
    print("0 - Sair\n")

    global estado    #  muda o estado de uso, ou seja, o usuário seleciona a opção
#    global opcao
    estado = input("Por favor, digite a opção desejada: ")
    if(int(estado)==0):
        print("\nObrigado por usar o GraphvizStore! Até a próxima!")
#    opcao = True

def criar_peca(nome):
        peca = Peca(nome)
        print( peca.toString() + " foi criado")

    # Aproveitando esse trecho para salvar a string num txt:
        f = open("pecas.txt", "a+")
        f.write(peca.toString()+"\n")
        f.close()


        return peca #O QUE O USUARIO ENTROU

def criando_pecas():
    pecas = []

    print("Digite 'sair' para sair: ")
    has_next = True
    while (has_next):
        pecaUser = input("Digite o nome da Peça: ")

        if (pecaUser == 'sair'):
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
    graph.show() #apresenta o graph





def inventario():  #Função para apresentar todos as peças registradas
    f = open("pecas.txt", "r") # Abertura obrigatória do arquivo
    lines = f.read().splitlines()  #Lê todas as linhas do txt
    print(lines) #Imprime todas as linhas sem o \n
    print("Numero de Linhas")
    print(len(lines)) # Mostra a quantidade de linhas
    f.close() #Fechamento obrigatório do arquivo


def teste_graph():
    from graphviz import Digraph, nohtml

    g = Digraph('g', filename='btree.gv',
                node_attr={'shape': 'record', 'height': '.1'})

    g.node('node0', nohtml('<f0> |<f1> G|<f2>'))
    g.node('node1', nohtml('<f0> |<f1> E|<f2>'))
    g.node('node2', nohtml('<f0> |<f1> B|<f2>'))
    g.node('node3', nohtml('<f0> |<f1> F|<f2>'))
    g.node('node4', nohtml('<f0> |<f1> R|<f2>'))
    g.node('node5', nohtml('<f0> |<f1> H|<f2>'))
    g.node('node6', nohtml('<f0> |<f1> Y|<f2>'))
    g.node('node7', nohtml('<f0> |<f1> A|<f2>'))
    g.node('node8', nohtml('<f0> |<f1> C|<f2>'))

    g.edge('node0:f2', 'node4:f1')
    g.edge('node0:f0', 'node1:f1')
    g.edge('node1:f0', 'node2:f1')
    g.edge('node1:f2', 'node3:f1')
    g.edge('node2:f2', 'node8:f1')
    g.edge('node2:f0', 'node7:f1')
    g.edge('node4:f2', 'node6:f1')
    g.edge('node4:f0', 'node5:f1')

    g.view()


def executar_dot(pathB):
    from graphviz import Source
#    pathA = 'C:/Users/OW/GraphvizStore/produto.dot'
    pathA = pathB
    s = Source.from_file(pathA)
    s.view()

def executar_lista(lista,ponto_de_acesso):

    f = open(ponto_de_acesso + ".dot", "w+")
    f.write("graph G {\n\t")
    for line in lista:
        f.write(line) # write line to output file
        f.write("\n")
    f.write("}")
    f.close()


def fdpclust():

    # fdpclust.py - http://www.graphviz.org/content/fdpclust

    from graphviz import Graph

    g = Graph('G', filename='fdpclust.gv', engine='fdp')

    g.node('e')

    with g.subgraph(name='clusterA') as a:
        a.edge('a', 'b')
        with a.subgraph(name='clusterC') as c:
            c.edge('C', 'D')

    with g.subgraph(name='clusterB') as b:
        b.edge('d', 'f')

    g.edge('d', 'D')
    g.edge('e', 'clusterB')
    g.edge('clusterC', 'clusterB')

    g.view()




def func1(arquivo, lista):
    print(arquivo, "com:", lista)

    acesso = pasta + "/Store/Produtos/Montagens/" + arquivo
    executar_lista(lista, acesso)

    file = open(pasta + "/Store/Produtos/Listas/" + arquivo + ".txt", "w+")
    for line in lista:
        # write line to output file
        file.write(line)
        file.write("\n")
    file.close()






def pega_pecas():
    produto = input("Digite o nome do produto: ")
    selectPecas = []

    f = open(pasta+"/Store/Peças/Peças.txt", "r") # Abertura obrigatória do arquivo
    listOfStrings = f.read().splitlines()  #Lê todas as linhas do txt
    buscar = True

    while (buscar):
        selection = input("Digite o nome da peça [ou 'sair()'] ")
        if(str(selection)== "sair()"):
            buscar = False
        else:
            if str(selection) in listOfStrings:
                print(selection, "é uma peça do inventário")
                selectPecas.append(selection)
            else:
                print(selection, "é não é uma peça do inventário")
                selectPecas.append(selection)



    f.close() #Fechamento obrigatório do arquivo

    func1(produto, selectPecas)
    print("Tchau, obrigado!")

while(int(estado) !=0 ):

    menu()

    if (int(estado)==1):
        pecas = criando_pecas()

    if (int(estado) == 2):
        desenhaGraph(pecas)

    if (int(estado) == 3):
        inventario()

    if (int(estado) == 4):
        entrada = input("Digite o nome do produto: ")

        endereco = pasta + '/Store/Produtos/Montagens/' + str(entrada) + ".dot"

        executar_dot(endereco)

    if (int(estado) == 7):
        teste_graph()

    if (int(estado) == 8):
        pega_pecas()