class Person:

    def __init__(self, name):
        self.name = name  # atributos de instancia
        self._energy = 100  # cuando se coloca el _ significa que es un atributo protegido

    # metodo protegido
    def _waste_energy(self, quantity):
        self._energy -= quantity


"""
Como tal, no existen los atributos o metodos protegidos en Python.
Estas practicas son mas por convension.
"""

person1 = Person("Jose")
print(person1.name)
print(person1._energy)
person1._waste_energy(20)
print(person1._energy)
