class Person:

    def __init__(self, name, age):
        self.name = name  # atributos de instancia
        self.age = age
        self.__password = "1234"  # el doble _ significa que es un atributo privado
        # para los atributos privados, Python hace name mangling _NOMBRECLASE_password
        # _person__password

    def __generate_password(self):
        return f"$${self.name}{self.age}"


"""
Al igual que con los protegidos, no existen en Python en si, y se hacen por convension
"""

person1 = Person("Jose", 24)
print(person1.name)

# print(person1.__password)  # esto dara error, ya que es un atributo privado
# esto si funciona, ya que es la forma de acceder a un atributo privado
print(person1._Person__password)

# print(person1.__generate_password()) # esto dara error, ya que es un metodo privado
# esto si funciona, ya que es la forma de acceder a un metodo privado
print(person1._Person__generate_password())
