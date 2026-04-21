# Truthy - valores verdaderos
# print(bool(True))  # True
# print(bool(1))  # True
# print(bool(123))  # True
# print(bool(1.1))  # True
# print(bool(-1))  # True
# print(bool(1j))  # True
# print(bool("Hola"))  # True
# print(bool([1, 2, 3]))  # True
# print(bool((1, 2, 3)))  # True
# print(bool({1, 2, 3}))  # True

# todo numero diferente a 0, es verdadero, incluso los negativos

# todo string diferente a vacio, es verdadero, incluso los espacios en blanco

# Falsey - valores falsos
print(bool(False))  # False
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(0j))  # False
print(bool(""))  # False
print(bool([]))  # False
print(bool(()))  # False
print(bool({}))  # False
print(bool(None))  # False

# todo el numero 0, es falso, incluso el 0 negativo

# todo string vacio, es falso, incluso los espacios en blanco