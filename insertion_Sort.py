def insertionSort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1

        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

# Testando com o lista de numeros: arr = [2, 5, 30, 15, 7, 20]

arr = [2, 5, 30, 15, 7, 20]

insertionSort(arr)
print(arr)


# Testando com o lista com 1000000 de elementos
import random
import timeit
def gerarLista(n):
    arr = []
    for i in range(n):
        elemento = random.randrange(100)
        arr.append(elemento)
    
    return arr

arr = gerarLista(100000)
print(arr)
start = timeit.timeit()
insertionSort(arr)
end = timeit.timeit()
print(arr)
print("{} Tamanho do Array ".format(len(arr)))
print ("{} sec Tempo de Ordenação do InsertionSort".format(end - start))

#output

# 100000 Tamanho do Array 
# -0.008046311002544826 sec Tempo de Ordenação do InsertionSort