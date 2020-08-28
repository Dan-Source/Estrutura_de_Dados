# Criando uma classe Node que ira conectar os dados
class Node:
    def __init__(self, data):
        self.esquerda = None
        self.direita = None
        self.data = data

class Arvore:
    def __init__(self):
        self.raiz = None

    def adicionar(self, node, valor):
        if(node == None):
            self.raiz = Node(valor)
        else:
            if (valor < node.data):
                if node.esquerda == None:
                    node.esquerda = Node(valor)
                else:
                    self.adicionar(node.esquerda, valor)
            else:
                if(node.direita == None):
                    node.direita = Node(valor)
                else:
                    self.adicionar(node.direita, valor)

    def imprimir(self, node):
        if (node != None):
            self.imprimir(node.esquerda)
            print(node.data)
            self.imprimir(node.direita)

def main():
    import random

    lista = []

    tamanho_da_lista = 0
    while(tamanho_da_lista < 20):
        numero_inteiro_par = random.randrange(100)
        if ((numero_inteiro_par % 2) == 0):
            lista.append(numero_inteiro_par)
            tamanho_da_lista+=1
    print(lista)

    arvore = Arvore()

    for i in range(len(lista)):
        arvore.adicionar(arvore.raiz, lista[i])

    print(arvore.imprimir(arvore.raiz))

main()