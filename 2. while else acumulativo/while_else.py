'''
while/else
CONTADORES
acumuladores
'''
"""
contador = 1
acumulador = 1  # acumula valores durante o laço
while contador <= 10:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador += 1
else:  # é executada ao WHILE ser falso
    print("cheguei ao else.")
"""

contador = 1  # conta de forma linear
acumulador = 1  # acumula valores durante o laço

while contador <= 10:

    print(contador, acumulador)

    if contador > 5:
        break  # após isso, executa o que está fora do laço

    acumulador = acumulador + contador
    contador += 1
else:  # é executada ao WHILE ser falso
    print("cheguei ao else.")

print("Isso será executado por está fora do laço.")


