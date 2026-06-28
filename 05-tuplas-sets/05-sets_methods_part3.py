# set1.symmetric_difference(set2) devuelve los valores que no forman parte de la interseccion de ambos sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

symmetric_difference = set1.symmetric_difference(set2)
# print(set1)
# print(set2)
# print(symmetric_difference)

# set1.issubset(set2) devuelve True o False dependiendo de si el valor del primer set se encuentra en el segundo
set1 = {1, 2}
set2 = {1, 2, 3, 4}
# print(set1.issubset(set2)) True
# print(set2.issubset(set1)) False

# set1.issupperset(set2) vendria siendo lo contrario a .issubset()
set1 = {1, 2, 3, 4}
set2 = {1, 2}
# print(set1.issuperset(set2)) True
# print(set2.issuperset(set1)) False
