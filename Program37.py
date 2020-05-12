# map function -> works with iterable object (list)

numbers = [1,2,3,4,5]


def square(a):
    return a*a


result = list(map(square, numbers))
print(result)


result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)