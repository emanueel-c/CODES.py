'''
EXPRESSÃO CONDICIONAL 'OR'
'''

'''
nome= "Emanuel"

if nome:
    print(nome)
else:
    print("You didn't typed your name!")
'''

nome = input("Qual seu nome? ")
print(nome or "You didn't typed your name!")  # if nome is true, will show nome
  # ele para na primeira expressão verdadeira.

a = 0
b = None
c = False
d = []
e = {}
f = 22  # stop in this number because is the only one True
g = "Luiz"

variavel = a or b or c or d or e or f or g  # if 'g' cames before 'f', it will be True
print(variavel)






















