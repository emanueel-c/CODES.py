'''
ELSE/FOR
'''

variavel = ['Emanuel', 'aJoão', 'Maria']
'''
comeca_c_j = False
for valor in variavel:
    if valor.lower().startswith("j"):  # desta forma, reconhece J e j. lower <- converteu -> valor
        comeca_c_j = True

if comeca_c_j:
    print("Começa com J.")
else:
    print("Não começa com J.")
    
'''

for valor in variavel:

    if valor.lower().startswith("j"):
        break
    print(valor)  # lê todos os valor e para, caso haja j.
else:
    print("Não existe palavra que comece com J.")
