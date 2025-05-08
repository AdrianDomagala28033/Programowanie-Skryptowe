import random
lista = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
for i in range(20):
    a = random.randint(0, 100)
    lista.append(a)
print(lista)
for i in lista:
    lista2.append(pow(i, 2))
print(lista2)
for i in lista:
    if(i % 2 == 0):
        lista3.append(i)
print(lista3)
for i in lista:
    lista4.append(bin(i))
print(lista4)
for i in lista:
    if(i >= 20 and i <= 50):
        lista5.append(i)
print(lista5)
s1 = []
for i in range(20):
    pass