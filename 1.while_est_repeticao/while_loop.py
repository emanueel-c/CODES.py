"""
WHILE - ESTRUTURA DE REPETIÇÃO
Utilizado para realizar ações enquanto uma condição for
verdadeira.
"""

    # ESTRUTURA REPRESENTATIVA
while condicao:
        pass

    # LOOP EM WHILE
while True:  # loop infinito por ser sempre verdadeiro
    nome = input('Qual o seu nome? ')
    print(f'Olá, {nome}!')
print('esse comentário nunca será representado')

    # OPERAÇÕES EM WHILE
i = 0
while i < 10:  # este é o laço while. DEBUGAR PARA ENTENDER MELHOR
    print(i)
    i = i + 1
print('Acabou!')  # só será printado quando o laço while/loop/ for False, ou seja, chegar em 10, pq 10 < 10 is False

    # CONTINUE EM WHILE
i = 0
while i < 10:
    i = i + 1  # reposicionei essa oper. pq em outro canto, o laço while ia ficar parado e em loop no numero 3
    if i == 3:
        continue  # ao usar isso, ele pula o bloco de codigo, pula pro proximo loop
    print(i)
print('Acabou!')

    # BREAK EM WHILE
i = 0
while i < 10:
    i = i + 1  # reposicionei essa oper. pq em outro canto, o laço while ia ficar parado e em loop no numero 3
    if i == 3:
        break  # ao usar isso, ele para o bloco de codigo, sai do loop, e n executa o proximo bloco
    print(i)
print('Acabou!')

    # ABAIXO, UM EXEMPLO DE UM LAÇO WHILE DENTRO DE OUTRO
x = 0  # coluna
while x <= 10:
    y = 0  # linha
    while y <= 5:  # ele fica dentro desse laço p/ dai partir p/ prox.
        print(f'{x},{y}')
        y += 1
    x += 1
print("Acabou!")