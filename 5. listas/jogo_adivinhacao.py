  # JOGO DE ADIVINHAÇÃO

secreto = "perfume"
digitadas = []
chances = 5

print("------------------------------------")
print("-------JOGO DE ADIVINHAÇÃO----------")
print("------------------------------------")

while True:
    letra = input("digite a letra: ")

    if len(letra) > 1:
        print("ah, isso não vale")
        continue  # assim não para o cod

    digitadas.append(letra)  # insere novo valor a digitadas

    if letra in secreto:
        print(f" issoooo, '{letra}' existe na palavra")
    else:
        print(f"'{letra}' não está contida na palavra secreta!")
        digitadas.pop()  # apaga ultima letra, a errada

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "*"

    if secreto_temporario == secreto:
        print(f"Que legal, você adivinhou! A palavra era {secreto_temporario}!")
        break
    else:
        print(f"a palavra secreta está assim: {secreto_temporario}")

    if letra not in secreto:
        chances -= 1
        print()
        print(f'você tem {chances} chances.')
        print()
        if chances == 0:
            print()
            print("Máximo de tentativas feitas.")
            break
