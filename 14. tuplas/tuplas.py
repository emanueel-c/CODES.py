'''
TUPLAS - Muito semelhante às listas, contudo ela tem seus elementos
imutáveis.
'''

# Exemplos de tuplas
t1 = 1, 2, 'a', 'Emanuel'
t2 =  (1,0,3,2,5,4, 'buzz')  # Tuplas podem estar ou não dentro de parenteses.
print(t2[4])  # Acessando algum valor pelo índice.


# Existe a possibilidade de alterar um valor dentro da tupla, mas tem que covertê-la
# para lista conforme abaixo
t3 = 12345, 54321, 'hello!'
t3 = list(t3)
t3[2] = 'fizz'
t3 = tuple(t3)  # Retornei para tupla após alterar o valor na lista.


# Tuplas também podem conter objetos mutáveis:
v = ([1, 2, 3], [3, 2, 1])


'''Um problema especial é a criação de tuplas contendo 0 ou 1 itens: a sintaxe usa 
certos truques para acomodar estes casos. Tuplas vazias são construídas por um 
par de parênteses vazios; uma tupla unitária é construída por um único valor e 
uma vírgula entre parênteses (não basta colocar um único valor entre parênteses). 
Feio, mas funciona. Por exemplo:'''

empty = ()
unitario = 'hello',
