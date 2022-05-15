def bubbleSort(lista):
    n = len(lista)
    for element in range(0,n-1):
        #removed the prints
        if lista[element] >= lista[element+1]:
            lista[element], lista[element+1] = lista[element+1], lista[element]
