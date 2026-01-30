



print("Hello World")

def greet(name):
    return f"Hello, {name}!"


while True:
    name = input("Enter your name (or 'exit' to quit): ")
    if name.lower() == 'exit':
        break
    greeting = greet(name)
    print(greeting)

print("Goodbye!")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"