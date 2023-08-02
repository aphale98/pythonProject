# Variables and Data Types
from animal import Person, Cat, Dog, make_sound

name = "Aman"
age = 25
height = 5.5
is_student = False

# Print statements
print("Hello, " + name)
print(f"I am {age} years old and {height} feet tall.")
print(f"Am I a student? {is_student}")

# Lists
fruits = ['apple', 'banana', 'cherry']
print("Fruits:", fruits)

# Loops
print("Fruits in the list:")
for fruit in fruits:
    print(fruit)

# Conditions
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# Functions
def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)
print("Result of addition:", result)

# Inheritance
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Siamese")

print(dog)
print(cat)

# Encapsulation
person = Person("Alice", 30)
person.greet()

# Polymorphism
animals = [dog, cat]
for animal in animals:
    make_sound(animal)
