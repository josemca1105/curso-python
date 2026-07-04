# los ciclos while son una estructura de control que permite ejecutar un bloque de código mientras se cumpla una condición. La sintaxis básica es la siguiente:
# while True:
#     # Esto imprimirá "Esto nunca se detendra" infinitamente hasta que se interrumpa el programa manualmente.
#     print("Esto nunca se detendra")  # loop infinito

# counter = 1
# while counter <= 5:
#     print(f"Number: {counter}")
#     counter += 1
# else:
#     print("Terminamos")

response = ''

while response.lower() != 'python':
    response = input("Escribe python para salir: ")

print('Terminamos')
