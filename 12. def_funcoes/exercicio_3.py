"""
RECEBE 2 VALORES E QUE O PRIMEIRO É UM VALOR, O SEGUNDO, UM PERCENTUAL.
RETORNE O VALOR DO PRIMEIRO SOMADO AO PERCENTUAL DO SEGUNDO
"""


def valores(valor, percentual):
    return valor, (percentual / 100) * valor + valor


ap = valores(2, 50)
print(ap)
ap = valores(78, 39)
print(ap)
# valores()
