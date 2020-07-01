'''
OPERAÇÕES TERNÁRIAS -
Substitui muito o uso do if - else no codigo.
'''

'''
if logged_user:
    msg = "Usuário logado"
else:
    msg = 'Usuário precisa logar."
'''

logged_user = False
msg = 'Usuário logado.' if logged_user else "Usuário precisa logar."
print(msg)

'''
idade = 17

if idade >=18:
    print("You can acess.")
else:
    print("You can't acess.")
'''
idade = 19
idade = "You can acess" if idade>=18 else "User can't acess the plataform"
print(idade)

  # DESSA FORMA ECONOMIZA-SE MUITO MAIS LINHAS 
idade_1 = input("Qual sua idade? ")
if not idade_1.isnumeric():
    print("O valor precisa ser numérico.")
else:
    idade_1 = int(idade_1)
    idade_1 = "VocÊ pode ter acesso" if idade_1 >=18 else "Você não tem acesso"
print(idade_1)









