from ast import arg


def decorator(func):
    def wrapper(*args, **kwargs):
        print("The Calculate Function is starting")
        print(f"The arguments are {args}")
        print(f"The keyword arguments are {kwargs}")
        result = func(*args, **kwargs)
        print(f"The result is {result}")
        print("The Calculate Function is ending")
    return wrapper

@decorator
def calculate(a, b):
    if a <= 0 or b <= 0:
        return "The numbers are not valid"
    if a > 100 or b > 100:
        return "The numbers are too large"
    if a % 2 == 0 and b % 2 == 0:
        return "The numbers are even"
    if a % 2 != 0 and b % 2 != 0:
        return "The numbers are odd"
    print("The Calculate Function is running")
    return a + b

calculate(11,20)