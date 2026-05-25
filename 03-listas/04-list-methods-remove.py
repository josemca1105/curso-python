numbers_lists = [1, 2, 3, 4, 5, 4, 5]
print(numbers_lists)

# pop() - Remueve el último elemento de la lista y lo devuelve
numbers_lists.pop()
numbers_lists.pop(1)  # Remueve el elemento en la posición 1 (el número 2)

# remove() - Remueve la primera aparición de un elemento específico
numbers_lists.remove(4)  # Remueve el número 4 de la lista

# clear() - Remueve todos los elementos de la lista
numbers_lists.clear()

print(numbers_lists)