# Logical operator -> and, or, not
# large number from 3 numbers using logical operator
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)

# vowel / consonant program
letter = input("Enter a letter : ")
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print("Vowel")
else:
    print("Consonant")