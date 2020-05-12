# Returning value from function


def add(a, b):
    return a + b


def largeNumber(a,b):
    return  a if a > b else b


maximum = largeNumber
result = add(10,20)
print(result)
print(maximum(20,30))