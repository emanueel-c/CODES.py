while True:
    print()
    num_1 = input("Insira um número: ")
    num_2 = input("Ok, agora o segundo número: ")
    print()
    print('OPERAÇÕES POSSÍVEIS +. -, *, / ')
    print()
    operacao = input(f"Insira agora a operação entre {num_1} e {num_2}: ")
    print()
    sair = input('Deseja sair ao terminar a operação? [y]es / [n]o? ')

    if not num_2.isnumeric() or not num_1.isnumeric():  # CASO OS NUMEROS INSERIDOS NÃO SEJAM NUḾERICOS!
        print(f"{num_1} e {num_2} não são númericos, por favor insira corretamente.")
        continue  # ISSO FAZ COM QUE O CÓDIGO NÃO DÊ ERRO NÃO EXECUÇÃO. 'BREAK' DARIA ERRO

    num_1 = float(num_1)
    num_2 = float(num_2)

    if operacao == '+' :
        print(num_2 + num_1)
    elif operacao == '-':
        print(num_1 - num_2)
    elif operacao == '*':
        print(num_1 * num_2)
    elif operacao == "/":
        print(num_1 / num_2)
    else:
        print()

    if sair == 'y':  # SE TIVESSE NO INICIO N DARIA CERTO, FECHARIA O CODIGO E N DARIA RESP. CASO [Y]
        break