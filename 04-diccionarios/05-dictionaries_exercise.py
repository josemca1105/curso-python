students = {
    "Ana": [8, 7, 9],
    "Luis": [15, 18, 10],
    "Sofía": [20, 20, 20]
}

# Agregar nuevo estudiante
# Sacar el promedio de un estudiante existente
# El promedio del estudiante nuevo

students["Jose"] = [18, 10, 9]
# print(students)

student = "Jose"
if student in students:
    # print(f"El alumno {student} existe")
    student_grades = students[student]
    total_grade = (student_grades[0] + student_grades[1] + student_grades[2]) / 3
    # print(total_grade)
    
    if total_grade >= 10:
        print(f"{student} aprobo con un promedio de: {total_grade:.2f}")
    else:
        print(f"{student} reprobo con una nota total de: {total_grade:.2f}")
    
else:
    print("Ese alumno no esta registrado")