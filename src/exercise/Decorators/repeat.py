def time(time):
    def decorator(func):
        def wrapper(a, b):
            print(f"Adding {a} and {b}")
            for _ in range(time):
                result = func(a, b)
            return result
        return wrapper
    return decorator

@time(3)
def add(a, b):
    print(f"Adding {a} and {b}")

print(add(10, 20))