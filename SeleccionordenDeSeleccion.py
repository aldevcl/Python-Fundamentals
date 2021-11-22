x = [8,5,2,6,9,3,1,4,0,7]

def selection_sort(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i+1,len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        if minimo != i:
            lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista

print(selection_sort(x))