from Peca import Peca

def criar_peca(nome,nome_arquivo):
        peca = Peca(nome)
        print( peca.toString() + " foi criado")

        acesso = "./Store/Listas/"+nome_arquivo + ".txt"

    # Aproveitando esse trecho para salvar a string num txt:
        f = open(acesso, "a+")
        f.write(peca.toString()+"\n")
        f.close()
        return peca #O QUE O USUARIO ENTROU



def criando_pecas():
    pecas = []

    arquivo = input("Digite o nome do produto:")

    print("\n Digite 'sair' para sair: ")
    has_next = True
    while (has_next):
        pecaUser = input("Digite o nome da Peça: ")

        if (pecaUser == 'sair'):
            has_next = False
        else:
            pecas.append(criar_peca(pecaUser, arquivo))

    return pecas