# Exceptions Handling -> try, except, finally (python)
# Run time errors, compile time errors

'''
# ZeroDivisionError -> 20 / 0
# TypeError
# ValueEroor -> 20 / a
# IndexError -> x = [10,20], print(x[3])

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
result = num1 / num2
print(result)
print("Done")


test = "Anis"
print(test[2])
print(test[4])
print("Done")

'''
try:
    list = [20,0,30]
    # result = list[0] / list[1]
    result = list[0] / list[3]
    print(result)

except ZeroDivisionError:
    print("Dividing by 0 is not possible")

except IndexError:
    print("Index is not found")

finally:
    print("done")