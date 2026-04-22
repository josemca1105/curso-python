# corto circuito

# El corto circuito es una técnica de programación que permite evitar la evaluación de una expresión lógica si el resultado ya se conoce.
# Esto se logra utilizando los operadores lógicos "and" y "or".

# De manera general, el corto circuito se utiliza para optimizar el rendimiento de un programa, evitando la ejecución de código innecesario.

# OR
# True or print("Hola Mundo")  # No se ejecuta la función print porque el resultado ya es True
# False or print("Hola Mundo")  # Se ejecuta la función print porque el resultado es False

# AND
# False and print("Hola Mundo")  # No se ejecuta la función print porque el resultado es False
# True and print("Hola Mundo")   # Se ejecuta la función print porque el resultado es True

name = False
print(name and name.upper())