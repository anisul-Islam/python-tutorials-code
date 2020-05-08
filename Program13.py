# Inner if statement
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

if num1 > num2:
    if num1 > num3:
        print("Large Number : ", num1)
    else:
        print("Large Number : ", num3)

if num2 > num1:
    if num2 > num3:
        print("Large Number : ", num2)
    else:
        print("Large Number : ", num3)
