# Metodos de adicion

numbers_list = [1, 2, 3, 4, 5]
print(numbers_list)

# append() - Adiciona un elemento al final de lista
numbers_list.append(100)
print(numbers_list)
# print(numbers_list.append(200))  # Devuelve None
numbers_list.append(200)
print(numbers_list)

# Insert
# insert() - Agrega un elemento en una posición específica
numbers_list.insert(1, 200)
numbers_list.insert(3, 300)

# Extends
# extend() - Agrega los elementos de una lista a otra lista
numbers_list.extend([11, 22, 33])

print(numbers_list)