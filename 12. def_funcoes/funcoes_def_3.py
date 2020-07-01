"""*ARGS - **KWARGS"""


def func(*args):  # * para existir vários parâmetros
    print(args)  # printará todos os parâmetros pedidos quando
                # chamar a FUNÇÃO


lista = [1,2,3,4,5]
print(*lista, sep="-")  # * desempacotando cada valor da lista e separado por "-"

# n1, n2, *n = lista  / (LISTAS/CONCEITO) n1 e n2 apareceram DESEMPACOTADAS,
# MAS O *n estarão em tuplas. *n é usado para mostrar todos os itens da lista



# TRABALHANDO DEF COM LISTAS


def func2(*args):  # * para existir vários parâmetros
    print(args)  # mostrará a lista contida em uma tupla
    print(args[0])  # acessado o primeiro item dos parâmetros
    print(args[-1])  # acessado o último item dos parâmetros
    print(len(args))  # CONTANDO QUANTOS PARÂMETROS EXISTEM DENTRO DA FUNÇÃO


func2(1,2,3,4,5)


#TUPLAS
# TUPLAS NÃO PODE SER ALTERADA, DIFERENTEMENTE DE LISTAS
# def func3(*args):
#     args[0] = 20  # TypeError: 'tuple' object does not support item assignment
#     print(args)
#
#
# func3(1,2,3,4,5)


def func4(*args):
    args = list(args)  # CONVERSÃO DE UMA TUPLA PARA O FORMATO LISTA!
    # para que assim possamos mudar os valores da tupla
    args[0] = 20
    print(args)


func4(1,2,3,4,5)


def func5(*args, **kwargs):  # KWARGS - KEYWORDS ARGUMENTS
    print(args)
    #print(kwargs['nome´], kwargs[sobrenome])  # unica forma de mostrar os KWARGS

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func5(*lista, *lista2, nome='Luiz', sobrenome="Otávio")
# NOME NEM SOBRENOME SERÁ PRINTADO, pq eles são arg. nomeados.
# CASO O COMANDO print(kwargs) SEJA POSTO, PRINTARÁ O KWARGS


#outras aplicações


def func6(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    #else:
        #print("idade não existe")  # caso queira omitir o erro,
        # so n usar o else

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func6(*lista, *lista2, nome='Luiz', sobrenome="Otávio", idade='30')

