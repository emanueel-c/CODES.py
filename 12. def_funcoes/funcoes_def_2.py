'''
FUNÇÕES (DEF) - PARTE 2
'''


def divisao(n1, n2):
    if n2 == 0:  # para não dar erro em div. p/ 0.
        return  # se for 0, sai da funcao e cai no else(line_14)
    return n1 / n2
# ao interpreter chegar em return ele não executa mais nada abaixo.


divide = divisao(8, 4)
if divide:
    print(divide)
else:
    print("Conta inválidade.")


def dumb():
    return [1,2,3]
# (line_19) aqui posso colocar qualquer valor e retorna o tipo
var = dumb()  # evitar tantos parenteses no print
print(var, type(var))