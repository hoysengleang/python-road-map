def myfunc(num):
    return lambda x: x * num

result = myfunc(10)
print("The result is", result)
print("The result is", result(2))