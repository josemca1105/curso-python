class Person:
    # cuando se escriben de la misma manera que las variables, significa que son atributos/metodos publicos
    species = "Humano"

    def __init__(self, name, age):
        self.name = name  # atributos de instancia
        self.age = age

    def work(self):
        return f"{self.name} esta trabajando muy duro"

    def eat(self, food):
        if food.lower() == "pizza":
            return "SUPERPOWERS"
        else:
            return "+Energia"


person1 = Person("Jose", 24)
print(person1.name)
print(person1.age)
print(person1.species)
print(person1.work())
print(person1.eat("hamburguesa"))
