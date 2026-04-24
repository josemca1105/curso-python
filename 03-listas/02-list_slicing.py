# List Slicing es una técnica que permite obtener una parte de una lista utilizando índices.
# La sintaxis básica para el slicing es: lista[inicio:fin:step]

# Ejemplo de slicing

shopping_cart = [
    'Camisas',
    'Tenis',
    'Calcetas',
    'Pantalones'
]

# [Inicio : Fin]
# print(shopping_cart[0:2])  # ['Camisas', 'Tenis']
# print(shopping_cart[1:3])  # ['Tenis', 'Calcetas']
# print(shopping_cart[1:4])  # ['Tenis', 'Calcetas', 'Pantalones']

# Crea una lista nueva con los elementos desde el índice 0 hasta el índice 1 (el índice 2 no se incluye)
# new_list = shopping_cart[1:3]
# print(new_list)
# print(shopping_cart)

# new_list[0] = 'Zapatos'
# print(new_list)
# print(shopping_cart)

# Los strings no se pueden mutar. Pero las listas sí, por lo que al modificar un elemento de la nueva lista,
# no se modifica el elemento original de la lista shopping_cart.

# new_list[1] = 'Collar'
# print(new_list)
# print(shopping_cart)

# shopping_cart[0] = 'Playera'
# print(shopping_cart)

# Copiar una lista
new_cart = shopping_cart[:]

print(shopping_cart)
print(new_cart)