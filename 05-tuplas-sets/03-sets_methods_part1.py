# conjuntos

# .add() agrega un elemento al set si no existe, si existe, el add es ignorado
my_set = {1, 2, 3}
my_set.add(6)  # lo agrega
my_set.add(3)  # es ignorado
my_set.add(5)

print(my_set)

# .remove() elimina un valor si existe, si no existe dara error
my_set.remove(2)
my_set.remove(6)
print(my_set)

# .discard() similar al .remove(), pero no marca error si no existe
my_set.discard(3)
my_set.discard(3)
my_set.discard(7)
print(my_set)

# .pop() elimina un elemento al azar y lo devuelve
print(my_set.pop())
print(my_set)
