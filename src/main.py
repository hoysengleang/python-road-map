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