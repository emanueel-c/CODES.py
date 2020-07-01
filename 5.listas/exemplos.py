'''
Listas em Python
FATIAMENTO
append, insert, pop, del, clear, extend, +
min, max
range
'''

l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l2)
l3 = l1 + l2  # concatenação das listas
l1.extend(l2)  # l1 extendeu a l2 nos valores
l2.append("b")  # insere um novo valor na lista
l2.insert(0, 'banana')  # inserindo banana do índice 0
print(l2)
l2.pop()  # remove o último item da lista
print(l2)

  #   0  1  2  3  4  5  6  7  8
l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del(l4[3:5])  # deleta os índices
print(l4)
print(max(l4))
print(min(l4))

l5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l5 = list(range(1, 10))
print(l5)

l6 = list(range(0, 100, 8))

for valor in l6:  #  iterando a lista
    print(valor)

l7 = [1,2,3,4,5,6,7,8,9]
soma = 0
for valor in l7:
    soma = valor + soma
    print(f'{soma} + {valor} = {soma}')
print(soma)

l8 = ['String', True, 10, 10.5]
for elem in l8:
    print(f'o tipo de elem é {type(elem)}, e o seu valor é {elem}')











