class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

    def __str__(self):
        return f"{self.name} is a {self.species}"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def __str__(self):
        return f"{self.name} is a {self.breed} {self.species}"


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed

    def make_sound(self):
        return "Meow!"

    def __str__(self):
        return f"{self.name} is a {self.breed} {self.species}"


# Encapsulation
class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age

    def greet(self):
        print(f"Hello, my name is {self._name} and I am {self.__age} years old.")


# Polymorphism
def make_sound(animal):
    print(animal.make_sound())
