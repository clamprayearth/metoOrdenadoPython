import random

n = int(input("Quantos elementos terá a lista? "))
with open("teste.txt", "w") as arquivo:
    txt = str(n)
    arquivo.write(txt)
ord = input("Usar (1)-SelectSort (2)-InsetionSort: (3)-BubbleSort")
with open("teste.txt", "a") as arquivo:
    txt = ord
    arquivo.write("\n"+txt)
for i in range(0,n):
    with open("teste.txt", "a") as arquivo:
        txt = str(random.randint(-n*2,n*6))
        arquivo.write("\n"+txt)
arquivo.close()