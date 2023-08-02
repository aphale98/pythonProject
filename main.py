# Variables and Data Types
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

# Conditionals
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# Functions
def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)
print("Result of addition:", result)
