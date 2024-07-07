def selectSort(ordenada):
    for i in range(0,len(ordenada)-1):
        minimo = ordenada[i]
        indx = i
        for j in range(i+1,len(ordenada)):
            #Caso o valor corrente seja menor ele será colcado na variavel minimo
            if (ordenada[j] < minimo):
                minimo = ordenada[j]
                indx = j

	    Coloca-se o valor do minimo na respectiva posição.
        ordenada[indx] = ordenada[i]
        ordenada[i] = minimo

    txt = "Lista ordenada é: {} "
    print(txt.format(ordenada))

#Entrada do numero de alementos da lista
ordenada = [] # Lista final
original = [] # Lista original
ordenada_sort = [] # Lista final ordenada com o metodo sort

n= int(input()) # Número de elementos da lista
ord = input()   # Decisão de qual metodo de ordenação a se utilizar
for i in range(0,n):
    num= int(input())
    ordenada.append(num)
    original.append(num)
    ordenada_sort.append(num)

#Chamada do metodo do sort
ordenada_sort.sort()
#Decisão de qual metodo utlizar
if ord == "1":
    selectSort(ordenada)

#Aqui é escrito dois arquivos com a lista ordenada com o algoritmo e outro com o metodo sort
for i in range(0,n):    
    with open("modelo.txt", "a") as arquivo1:
        arquivo1.write(str(ordenada_sort[i])+"\n")
    with open("resultado.txt", "a") as arquivo2:
        arquivo2.write(str(ordenada[i])+"\n")

#Impressão da lista obtida no arquivo teste.txt
txt = "Lista digitada: {} "
print(txt.format(original))