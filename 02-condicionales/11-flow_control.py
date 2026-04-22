# El control de flujo en Python se refiere a la forma en que se ejecutan las instrucciones en un programa.
# Las estructuras de control de flujo permiten tomar decisiones y repetir bloques de código según ciertas condiciones.

edad = int(input("Introduce tu edad: "))

if edad < 0:
    print("La edad no puede ser negativa.")
elif edad <= 12:
    print("Eres un infante.")
elif edad <= 17:
    print("Eres un adolescente.")
elif edad <= 64:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")