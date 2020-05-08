# ternary operator
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
'''
if num1 > num2:
    print(num1)
else:
    print(num2)
'''
print(num1 if num1 > num2 else num2)