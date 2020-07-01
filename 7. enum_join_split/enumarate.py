'''
ENUMERATE
'''
'''
string = "O Brasil é penta"
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])
'''
 #desempacotamento
lista = ['Luiz', 'João', 'Maria']

for indice, nome in enumerate(lista):  # enumeração da lista
    print(indice, nome)

lista2 = ['Luiza', 'aJoão', 'aMaria']

n1, n2, n3 = lista2

print(n2)


