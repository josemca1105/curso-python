# range() - permite iterar segun el valor asignado al rango
numbers = list(range(200)) # genera una lista que va desde el 0 al 199

# print(numbers)

# join() - junta las sentencias que le pasan en una sola cadena de texto
sentence = ' '.join(['Hola', 'Mundo', 'desde', 'un', 'join,', 'besos']) 
# print(sentence)

# sum() - suma el contenido de la variable iterable que se le indica
# max() - devuelve el mayor valor entre el contenido de la variable
# min() - devuelve el menor valor entre el contenido de la variable
# len() - devuelve la cantidad de valores que tiene la variable

total = sum(numbers)
max_number = max(numbers)
min_number = min(numbers)
elements = len(numbers)
print(total)
print(max_number)
print(min_number)
print(elements)