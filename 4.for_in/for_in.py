'''
FOR IN EM PYTHON / coisas finitas
ITERANDO STRINGS COM FOR
FUNÇÃO RANGE (start=0, stop, step=1)
'''

# forma menos pŕatica
text_2 = "Python"
c = 0
while c < len(text_2):
    print(text_2[c])
    c += 1

# INDICE EM PYTHON COM FOR-in
text = 'Python'
for n, letra in enumerate(text):
    print(n, letra)

# FUNÇÃO RANGE
for number in range(0, 10, 1):  # = (10)
    print(number)
    
'''
#forma de se achar multiplos atraves do range
'''
# regressiva
for number in range(20, 10, -1):  # = (10)
    print(number)
print("#######")

# achar multiplo
for n in range(100):
    if n % 8 == 0:
        print(n)
print("#######")

for n in range(0, 100, 8):
    print(n)

# POR A LETRA DE UM TEXTO MAIUSCULA
text = "python"
new_string = ''
for letter in text:
    if letter == 't':
        new_string += letter.upper()
    elif letter == 'h':
        new_string += letter.upper()
    else:
        new_string += letter
print(new_string)

