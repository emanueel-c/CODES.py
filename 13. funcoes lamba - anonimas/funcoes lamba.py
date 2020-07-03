'''
Comumente é usado as funções def, porém existe
As funções anônimas que é usado quando vc precisa 
passar uma função por parametro para outra 
função/metodo/classe.
''' 


def funcao(arg, arg2):
    return arg * arg2

var = funcao(2,2)

print(var)


# É a mesma coisa, contudo de uma diferente forma.
a = lambda x, y: x * y

print(a(2,3))


# Exemplo prático

lista = [
    ['P1', 13],
    ['P2', 3],
    ['P3', 43],
    ['P4', 21],
    ['P5', 32],
]

# ou seja, não precisei criar uma função só p ordenar uma lista
lista.sort(key=lambda item: item[1], reverse=True)
print(lista)
# sort serve para ordenar a LISTA


