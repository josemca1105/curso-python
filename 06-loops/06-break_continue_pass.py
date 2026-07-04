# pass: ayuda a pausar la implementacion para continuarla a futuro sin afectar la ejecucion del codigo
for item in [1, 2, 3, 4, 5]:
    pass

# break: rompe el programa al llegar a la linea de codigo donde se ejecuta
# for item in [1, 2, 3, 4, 5]:
#     if item == 4:
#         break
#     print(item)

# continue: ignora un pedazo del ciclo
number = 0

while number < len([1, 2, 3, 4, 5]):
    number += 1
    continue
    print(number)
