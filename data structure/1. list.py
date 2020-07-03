"""
MORE ON LISTS
"""

# APPEND - list.append(x)
# Adiciona um item ao fim da lista.
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l2.append("b")  # insere um novo valor na lista


# EXTEND - list.extend(iterable)
# Prolonga a lista, adicionando no fim todos os 
# elementos do argumento iterable passado como 
# parâmetro.
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)  # l1 extendeu a l2 nos valores
"""
Um objeto é iterable quando você pode percorrer 
seus valores usando um “for valor in objeto”. 
Se o objeto for iterável, ele é retornado. 
Se não, a exceção TypeError é levantada
"""


# INSERT - list.insert(i, x)
# Insere um item em uma dada posição. O primeiro 
# argumento é o índice do elemento antes do qual 
# será feita a inserção
l2 = [4, 5, 6]
l2.insert(0, 'banana')  # inserindo banana do índice 0


# REMOVE - list.remove(x)
# Remove o primeiro item encontrado na lista cujo valor 
# é igual a x. Se não existir valor igual, uma exceção 
# ValueError é levantada.
l1 = [1, 2, 3]
l1.remove(2)


# POP - list.pop([i])
# Remove um item em uma dada posição na lista e o retorna. 
# Se nenhum índice é especificado, a.pop() remove e devolve 
# o último item da lista. (Os colchetes ao redor do i na 
# demonstração do método indica que o parâmetro é opcional, 
# e não que é necessário escrever estes colchetes ao chamar 
# o método.
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.pop()
l2.pop([i])


# COUNT - list.count(x)
# Devolve o número de vezes em que x aparece na 
# lista
l1 = [1, 2, 3, 2 , 3, 2, 2, 2]
l1.count(2)  # conta qts 2 aparecem

