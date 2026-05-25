letters = ['a', 'b', 'm', 'o', 'c', 'z', 'g', 'd', 'e']
print(letters)

# sort() - Ordena la lista de menor a mayor / en este caso seria en orden alfabetico
letters.sort()
# print(letters)

# sorted() - Devuelve una nueva lista ordenada de menor a mayor / en este caso seria en orden alfabetico
# new_letters = sorted(letters)
# print(new_letters)
# print(letters)

# como hacerlo pero sin sorted

# new_letters = letters[:] # list slicing para crear una nueva lista con los mismos elementos
# new_letters.sort()
# print(new_letters)

new_letters = letters.copy() # metodo copy para crear una nueva lista con los mismos elementos
new_letters.sort()
# print(new_letters)

# reverse() - Ordena la lista de mayor a menor / en este caso seria en orden alfabetico inverso
letters.reverse()
print(letters)