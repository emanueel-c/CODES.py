"""
DESEMPACOTAMENTO DE LISTAS
"""

lista = ['Luiz', 'João', 'Maria', 1,2,3,4,5,6]

n1, n2, *lista_restante, ultimo_da_lista = lista  # para os demais valores presentes na lista

print(n1, n2, lista_restante)
print(ultimo_da_lista)
