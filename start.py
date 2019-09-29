from Graphviz import Graphviz
from Lista.Criar_lista import criando_pecas

estado = 100
opcao = False

pasta = './'

def menu():

    print("--- Bem-vindo ao GraphvizStore ----\n")
    print("Menu de opções")
    print("1 - Adicionar peças")
    # print("2 - Criar relacionamentos")
    # print("3 - Consultar peças")
    # print("4 - Consultar relacionamentos")
    # print("5 - Excluir peça")
    # print("6 - Editar peças")
    print("0 - Sair\n")

    global estado    #  muda o estado de uso, ou seja, o usuário seleciona a opção
#    global opcao
    estado = input("Por favor, digite a opção desejada: ")
    if(int(estado)==0):
        print("\nObrigado por usar o GraphvizStore! Até a próxima!")
#    opcao = True


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



while(int(estado) !=0 ):

    menu()

    if (int(estado)==1):
        pecas = criando_pecas()

    if (int(estado) == 2):
        desenhaGraph(pecas)

    if (int(estado) == 3):
        inventario()