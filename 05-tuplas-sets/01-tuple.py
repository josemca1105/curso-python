my_tuple = (1, 2, 3, 4, "Hola", True, 2, "Hi", 5, 4, 3, 2)

print(my_tuple)

"""
1. Es ordenadaL: tiene un indice al igual que las listas

2. Son inmutables: no puede ser cambiada luego de ser creada

3. Permite duplicados: por ejemplo, tener varias veces el 2

4. Son indexadas
"""

# Tienen pocos metodos:
# .count() - cuenta cuantos elementos hay en la tupla
# print(my_tuple.count(2))

# .index() - devuelve en que posicion esta el valor especificado. si el valor se repite, como el 2, devuelve la primera posicion donde aparece
# print(my_tuple.index(2))

# my_tuple[4] = "Mundo"  # Esto no se puede, da error dado a que las tuplas son inmutables
new_tuple = my_tuple[4]
print(new_tuple)