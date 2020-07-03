"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""


def value(n1):
    if n1 % 2 == 0:
        print("fizz")
    elif n1 % 5 == 0 and n1 % 3 == 0:
        print("fizzbuzz")
    elif n1 % 5 == 0:
        print("buzz")
    else:
        return f"{n1}"



var = value(12)
print(var)
# pro codigo acontecer e rodar,
# tenho que chamar a def


'''
CODIGO MAIS LIMPO DE ACORDO C/ O CURSO
'''


def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz, {n} é divisível por 3 e 5'
    if n % 5 == 0:
        return f'buzz, {n} é divisível por 5'
    if n % 3 == 0:
        return f'fizz, {n} é divisível por 3'
    return n


from random import randint  # importando numeros aleatorios para
# usar com a def

for i in range(100):
    aleatorio = randint(0, 100)  # numeros de 0 a 100
    print(fb(aleatorio))
