# Registro
# Recibir de manera dinamica el nombre, el año de nacimiento, correo, y clave

"""
    Nombre: Jose
    Email: jose@correo.com
    Tendras XX años en el 2050
    Tu contraseña es: ********
"""

name = str(input("Ingrese su nombre: "))
birth_year = int(input("Ingrese su año de nacimiento: "))
email = str(input("Ingrese su correo: "))
password = str(input("Ingrese su contraseña: "))

future_age = 2050 - birth_year
password_length = len(password)

result = f"""
    Nombre: {name}
    Email: {email}
    Tendras {future_age} años en el 2050
    Tu contraseña es: {'*' * password_length}
"""

print(result)