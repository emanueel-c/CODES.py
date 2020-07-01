'''
FUNCOES - def em Python (parte 1)
DEF GERALMENTE É USADA PARA AJUDAR A DIMINUIR REPETIÇÕES NO CODIGO (UMA ROTINA)
'''

'''
def funcao():  # def é usado pra vc definir suas proprias funcoes.
    print("Hello World!")

ao se usar def é mais pratico quando vc quer mudar algo dentro da str, por
exemplo, e todos os valores dentro da variavel mudarão quando vc chama 
funcao. EVITA REPETICAO.

funcao()
funcao()
funcao()  # printando 3 vezes HW.
'''

def saudacao(msg = 'Hello, ', name = 'User'):  # using parameters inside saudacao
    name = name.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, name)  # isn't usual on programming, it's just an example


saudacao(name = 'Emanuel', msg = 'Hi, ')
saudacao()
saudacao()


# PARAMETROS SAUDACAO
def saudacao(msg = 'fala, ', name = 'manel'):  # using parameters inside saudacao
    name = name.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg}, {name}'


variable = saudacao()
print(variable)


# PARAMETRO PARA ORGANIZAÇÃO
def lin(msg):  # o parametro é a msg que vou colocar
    print("-" * 30)
    print(msg)
    print("-" * 30)


lin("emanuel é lindo")

# USANDO DIVERSOS PARAMETROS
def contador(* num):
    for valor in num:
        print(f' {valor} ', end='')
    print('FIM!')


contador(2, 3, 4)  # mostrando em tuplas
contador(2)
contador(2, 3, 5, 6, 7, 2)

# OUTRA FORMA
def cont(*number):
    tam = len(number)
    print(f"Recebi os valores {number} e são ao todo {tam} números")


cont(2, 3, 4)  # mostrando em tuplas
cont(2)
cont(2, 3, 5, 6, 7, 2)

# DESEMPACOTAMENTO COM PARAMETROS
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(2,4)
soma(2, 3, 6 ,8)

# EXAMPLE
def greet(languague):  # greet = cumprimento
    if languague == "es":
        print("Hola")
    elif languague == "fr":
        print("Bonjour")
    else:
        print("Hello.")

