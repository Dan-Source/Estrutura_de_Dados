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

for i in range(len(arr)): 
    print ("% d" % arr[i])


# Testando com o lista com 1M de elementos
import random
import timeit
def gerarLista(n):
    arr = []
    for i in range(n):
        elemento = random.randrange(n)
        arr.append(elemento)
    
    return arr


arr = gerarLista(1000000)
start = timeit.timeit()
insertionSort(arr)
end = timeit.timeit()

print("{} Tamanho do Array ".format(len(arr)))
print ("{} sec Tempo de Ordenação do InsertionSort".format(end - start))