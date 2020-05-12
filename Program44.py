# Exceptions Handling -> except, raise

try:
    num1 = int(input("Enter 1st number : "))
    num2 = int(input("Enter 2nd number : "))
    result = num1 / num2
    print(result)

except ValueError:
    print("Please enter only number")
except ZeroDivisionError:
    print("You can not divide a number by 0")

finally:
    print("Thank you!!!")

'''
# multiple exception can be put together
except (ValueError, ZeroDivisionError):
    print("Incorrect Input")
'''

# raise exception
def voter (age):
    if age < 18:
        raise ValueError("Invalid voter")
    return "You are allowed to vote"


try:
    print(voter(19))
    print(voter(16))
except ValueError as e:
    print(e)

