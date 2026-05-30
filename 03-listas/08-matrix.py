# una matriz es una coleccion de coleccions / es una lista de listas

matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [9, 8, 7]
]

# print(matrix) # muestra toda la lista
# print(matrix[1]) # muestra la columna 2 donde se encuentra el 4
print(matrix[1][1]) # muestra unicamente el valor 4

# como las listas son mutables, se puede cambiar el valor de un campo en particular
matrix[1][1] = 10
print(matrix[1][1])
print(matrix)