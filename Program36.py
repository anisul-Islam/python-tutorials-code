# lambda function -> anonymous function (without name) , works with single line code

# named function
def calculate(a,b):
    result = (a*a) + 2*a*b + b*b
    return result


def cube(x):
    return x * x * x


# lambda parameter : expression
a = (lambda a, b: (a*a) + 2 * a * b + b * b)(2, 3)


cubeNumbers = (lambda x : x * x * x) (2)

print(a)
print(calculate(2,3))
print(cube(3))
print(cubeNumbers)