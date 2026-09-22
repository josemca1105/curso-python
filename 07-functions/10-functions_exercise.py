#  letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#  numeros = "0123456789"
#  simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
# caracteres = letras + numeros + simbolos
# Formula simple: (item * 7 + 3) % len(caracteres)

# Entrada: 8
# Salida : &D^#23SN

import random
import string

def password_generator(longitud):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(longitud))
    return password

longitud = int(input("Por favor ingresa cuantos caracteres tendra la clave: "))
print("Clave cifrada: ", password_generator(longitud))