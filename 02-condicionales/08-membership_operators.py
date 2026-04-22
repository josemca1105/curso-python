# in

# not in

# Son utilizados para verificar si un elemento se encuentra o no en una secuencia (como una lista, tupla, cadena, etc.).
# Devuelven True o False según corresponda.

# print(9 in range(1, 10))  # Verifica si el número 9 está en la secuencia del 1 al 9 (True)
# print(10 in range(1, 10)) # Verifica si el número 10 está en la secuencia del 1 al 9 (False)
# print(10 in range(1, 11)) # Verifica si el número 10 está en la secuencia del 1 al 10 (True)

fruits = ["Manzana", "Banana", "Fresa"]
# print("Fresa" in fruits)  # Verifica si "Fresa" está en la lista de frutas (True)
# print("Naranja" in fruits) # Verifica si "Naranja" está en la lista de frutas (False)
# print("Mango" in fruits) # Verifica si "Mango" está en la lista de frutas (False)
# print("Fresa" not in fruits)  # Verifica si "Fresa" no está en la lista de frutas (False)

sentence = "Soy programador en Python, Golang, PHP, ..."
print("Python" in sentence)  # Verifica si "Python" está en la cadena (True)
print("Mongo" in sentence)   # Verifica si "Mongo" está en la cadena (False)