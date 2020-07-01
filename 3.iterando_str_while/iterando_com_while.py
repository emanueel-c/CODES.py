'''
iterando strings com while
iterar um objeto - significa que você vai percorrer cada elemento do obj.
'''


while True:
    frase_ex_str = input("Frase/letras: ")  # contar as letras que mais aparecem
    tamanho_str = len(frase_ex_str)
    contador = 0
    vezes_que_aparece = 0
    letra_mais_frequente = ''  # retorna um valor boolean falso ""

    while contador < tamanho_str:
        qtd_vezes_letra = frase_ex_str.count(frase_ex_str[contador])

        if vezes_que_aparece < qtd_vezes_letra and frase_ex_str[contador].strip():
            letra_mais_frequente = frase_ex_str[contador]
            vezes_que_aparece = qtd_vezes_letra

        contador += 1
    print(letra_mais_frequente, vezes_que_aparece)

# PARA USAR O LAÇO REPETIDA VAZES PARA PÔR COMANDO, USA-SE TAMBÉM O 'INPUT' C/ 'WHILE TRUE'
# strip() - serve p tirar espaço
# print(minha_string.count("a"))  # serve pra contar quantas vezes ocorreu "a" letra na str.

'''#  CONTAR STR. PELOS ÍNDICES
minha_str = 'o rato roeu a roupa do rei de roma'
tamanho_str_2 = len(minha_str)
c = 0
while c < tamanho_str_2:
    print(c, minha_str[c])
    c += 1'''



