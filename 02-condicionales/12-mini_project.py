# Instrucciones:

# Crear un programa de evaluacion de candidatos potenciales con conocimientos en Python para RH.
# Obtendras el nombre, años de experiencia y habilidades.

# Evaluaras:
# * Si el candidato sabe Python/Django, tiene +3 años de experiencia: Candidato Optimo
# * Si el candidato sabe Pytrhon/Django, tiene +1 año de experiencia: Buen Candidato
# * Si el candidato sabe Python/Django: Posible Candidato
# * Si el candidato no sabe Python: No optimo, se guardara CV

# Consejo: Ocupa los metodos split()
# numbers = "1,2,3"
# numbers.split(",") -> ["1", "2", "3"]

# Solicitar el nombre del candidato
name = input("Ingrese el nombre del candidato: ")
experience = int(input("Ingrese los años de experiencia del candidato: "))
skills = input("Ingrese las habilidades del candidato, separadas por comas (ej: Python, Laravel, Java, etc.): ").split(",")

# Evaluar si el candidato tiene conocimientos en Python o Django
evaluate_skills = "Python" in skills or "Django" in skills

# Evaluar el resultado y mostrarlo al usuario
result = ""
if evaluate_skills:
    if experience >= 3:
        result = "Candidato Optimo"
    elif experience >= 1:
        result = "Buen Candidato"
    else:
        result = "Posible Candidato"
else:
    result = "No optimo, se guardara CV"

# Mostrar el resultado al usuario
print(f"El candidato {name} es: {result}")