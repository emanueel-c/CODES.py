'''
* JOIN - Juntar uma lista  #str
'''

string = "O Brasil é penta."
lista = string.split(' ')
print(lista)


string = "O Brasil é penta."
lista = string.split(' ')  # separação str
string2 = ','.join(lista)  # junta a nova str2 com o comando join(lista)

print()

print(string)
print(lista)
print(string2)

