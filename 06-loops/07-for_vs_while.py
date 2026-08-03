# For: para iterables (listas, tuplas, diccionarios, sets, strings)
# While: para condiciones (booleanas) cuya longitud es desconocida

my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)

item = 0
while item < len(my_list):
    print(item)
    item += 1
