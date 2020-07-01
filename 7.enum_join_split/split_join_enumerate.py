'''
SPLIT, JOIN, ENUMERATE
* SPLIT - Dividir uma string #str
* JOIN - Juntar uma lista  #str
* ENUMERATE - Enumerar os elementos de lista  #list / iteráveis
'''

string = "O brasil a a a a a a  é o país do futebol, o brasil é penta"
lista1 = string.split(" ")  # espaço
lista2 = string.split(',')  # virg

palavra = ''
contagem = 0
for valor in lista1:  # iterando
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f"A palavra que apareceu mais vezes é -{palavra}- ({contagem}x)")
