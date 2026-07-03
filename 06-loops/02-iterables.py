numbers = [1, 2, 3, 4, 5]

# iterables: son los objetos que pueden ser recorridos en un bucle, como listas, tuplas, diccionarios, conjuntos, etc.
# iterador: es el objeto que se obtiene al llamar a la función iter() sobre un iterable. Este objeto tiene un método __next__() que devuelve el siguiente elemento del iterable.
# for number in numbers:
#     print(number)

iterator = iter(numbers)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# si se agrega una llamada más a next(iterator) se lanzará una excepción StopIteration, ya que no hay más elementos en el iterable.

user = {
    'name': 'Jose',
    'age': 24,
    'can_swim': False
}

for key, value in user.items():
    print(key, value)
