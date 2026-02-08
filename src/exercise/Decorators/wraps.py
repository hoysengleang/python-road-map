from functools import wraps

def decor(func):
    @wraps(func)
    def wrapper(a, b):
        print("Hello World")
        result = func(a,b)
        return result
    return wrapper



@decor
def greet(name):
    return f"Hello {name}"

print(greet.__name__)
        