def bubbleSort(lista):
    n = len(lista)
    for element in range(0,n-1):
        print(lista[element],lista[element+1])
        if lista[element] >= lista[element+1]:
            lista[element], lista[element+1] = lista[element+1], lista[element]
            print(lista[element],lista[element+1])
