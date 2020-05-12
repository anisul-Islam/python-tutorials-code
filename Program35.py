# debugging
def addition(*numbers):
    sum = 0
    for x in numbers:
        sum = sum + x
    return sum


print(addition(10,20))
print(addition(10,20, 30))
