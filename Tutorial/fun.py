'''A function in Python is a block of reusable code that 
performs a specific task.
It helps to reduce code repetition, 
improve readability, and make programs easier to manage.'''

# Usage: Simple function without parameters
def greet():
    print("Hello, welcome to Python functions!")

greet()
 

# Usage: Function with one parameter
def greet_user(name):
    print("Hello", name)

greet_user("System Shield")


# Usage: Function with multiple parameters
def add_numbers(a, b):
    print("Sum:", a + b)

add_numbers(10, 20)


# Usage: Function with return value
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print("Multiplication:", result)
