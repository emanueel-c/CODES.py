"""
crie um prog. que tenha a função chamada voto,
que vai receber como parametro o ano de nascimento
de uma pessoa, retornando um valor literal indicando
se a pessoa tem  o voto NEGADO, OPCIONAL, OU
OBRIGATORIO NAS ELEIÇÕES
"""

while True:


    def voto(ano_nasc):
        # negado - 16, opcional + 60, obrigatorio 18 e 60
        ano_atual = 2020
        if ano_atual - ano_nasc < 16:
            return f'Com {ano_atual - ano_nasc } anos, o voto é: NEGADO.'
        if ano_atual - ano_nasc >= 18 and ano_atual - ano_nasc < 60:
            return f'Com {ano_atual - ano_nasc } anos, o voto é: OBRIGATÓRIO'
        if ano_atual - ano_nasc >= 60:
            return f'Com {ano_atual - ano_nasc } anos, o voto é: OPCIONAL.'


    var = voto(int(input("Ano de nascimento: ")))  # aqui criei uma nova variavel para que pudesse haver um print
    # portanto, chamei a função voto, que por sua vez, usei da função input para que o usuário colocasse o ano de nasc.
    print(var)



