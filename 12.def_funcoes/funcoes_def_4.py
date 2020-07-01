"""
aqui temos alguns possiveis problemas com defs
"""

variavel = 'valor'  # chamamos essa variavel de VARIÁVEL GLOBAL


def func():
    print(variavel, " - func1")


def func2():
    variavel = 'outro valor'
    print(variavel, " - func2")


func()
func2()
print(variavel, " - var global")  # há de se pensar que por se ter mudado o valor da variavel
# dentro da def func2, contudo, a variavel da func2 só foi alterado localmente
# ou seja, somente dentro da função. PORTANTO, DARÁ PRINT NA VARIAVEL GLOBAL (LINE - 5)



# você não consegue alterar o valor de uma variavel global dentro de uma função
# a não ser que:


def func3():
    global variavel
    # forma de alterar a var glob.
    # AVISO - ESSA PRATICA É ALGO TOTALMENTE NÃO ACONSELHÁVEL POR PODER BUGAR SEU PROGRAMA.
    variavel = 'outro valor'
    print(variavel, " - func3")


func3()



# melhor forma de se usar parametros, retornar valor, n alterando valores de var glob.


def func4(arg = None):
    arg = arg.replace("v", "c")
    return arg


outra_var = func4(arg = variavel)
print(outra_var, " - func4")




# POSSIVEIS ERRO

var2 = "bebê"


def func5():
    #print(var2)  # aqui é dará o erro
    # UnboundLocalError: local variable 'var2' referenced before assignment
    var2 = 123  # não posso usar uma var global e depois mudar o valor dela
    print(var2)

func5()


# ERRO DE USAR UMA VARIAVEL CHAMANDO-AS DENTRO DE DUAS DEF


def fun6():
    outra_var2 = 'emanuel'



def fun7():
    print(outra_var2)


fun6()
func7()
























