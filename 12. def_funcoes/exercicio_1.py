'''
crie uma função que exibe uma saudação com os parametros saudação e nome
'''


def boas_vindas(saudacao = 'olá', nome = 'Emanuel'):
    return f'{saudacao}, {nome}'


var_bv = boas_vindas()
print(var_bv)  # chamando a def