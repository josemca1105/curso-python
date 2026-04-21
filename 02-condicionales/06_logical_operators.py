# # Evaluar condiciones

# # and - va a evaluar si dos o mas condiciones son verdaderas
# # Si todas las condiciones son verdaderas, el resultado es verdadero. Si alguna de las condiciones es falsa, el resultado es falso.
# print(True and True) # True
# print(True and False) # False
# print(False and True) # False
# print(False and False) # False

# # or - va a evaluar si al menos una de las condiciones es verdadera
# # Si al menos una de las condiciones es verdadera, el resultado es verdadero. Si todas las condiciones son falsas, el resultado es falso.
# print(True or True) # True
# print(True or False) # True
# print(False or True) # True
# print(False or False) # False

# # not - va a invertir el valor de una condición
# # Si la condición es verdadera, el resultado es falso. Si la condición es falsa, el resultado es verdadero.
# print(not True) # False
# print(not False) # True

# Ejemplos

# and
age = 23
licensed = True

if age >= 18 and licensed:
    print("Puedes conducir")
    
# or
is_student = False
membership = True

if is_student or membership:
    print("Obtienes un descuento especial")
    
# not
is_admin = False

if not is_admin:
    print("Acceso denegado")