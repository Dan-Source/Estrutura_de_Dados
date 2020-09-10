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
    
    def buscar(self, node, valor):
        if valor <  node.data:
            if node.esquerda is None:
                return str(valor)+" não encontrado."
            return self.buscar(node.esquerda, valor)
        if valor >  node.data:
            if node.direita is None:
                return str(valor)+" não encontrado."
            return self.buscar(node.direita, valor)
        else:
            return str(node.data) + " encontrado"
    
    def encontrarMenor(self, node):
        n = node
        while(n.esquerda is not None):
            n = n.esquerda 
        print(str(n.data) + " menor numero da arvore")
    def encontrarMaior(self, node):
        n = node
        while(n.direita is not None):
            n = n.direita
        print(str(n.data) + " maior numero da arvore")


def main():
    import random

    lista = [101]

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

    arvore.imprimir(arvore.raiz)

    print(arvore.buscar(arvore.raiz, 9))
    print(arvore.buscar(arvore.raiz, 10))
    
    arvore.buscar(arvore.raiz, 101) # não encontrado
    arvore.encontrarMaior(arvore.raiz)
    arvore.encontrarMenor(arvore.raiz)

main()