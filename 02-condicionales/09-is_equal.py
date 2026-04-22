# == Equal o igualdad

# print(5 == 5) # True
# print(True == 1) # True
# print('' == 1) # False
# print([] == 1) # False
# print(10 == 10.0) # True

new_list = []
other_list = []

# print(new_list == other_list) # True

# is compara en memoria, no en valor, es decir, si ambos objetos son el mismo objeto en memoria
print(new_list is other_list) # False, porque son objetos diferentes en memoria
print(new_list == other_list) # True, porque ambos son listas vacías