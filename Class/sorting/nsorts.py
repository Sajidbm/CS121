#the comments help troubleshoot
def bubbleSort(lista):
    n = len(lista)
    for turn in range(n,1,-1):
        #print("Outer:"+str(turn)+"\n")
        #print("-")
        for element in range(turn-1):
            #the choice of range: if it's not turn-1 then we go out of the range
            print(element)
            if lista[element] >= lista[element+1]:
                lista[element], lista[element+1] = lista[element+1], lista[element]
