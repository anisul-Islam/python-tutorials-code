# Letter Grade program using logical operator
# short circuit evaluation
marks = int(input("Enter your marks : "))
if marks > 100 or marks < 0:
    print("Invalid marks")
elif 80 <= marks <= 100:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("A-")
elif marks >= 50:
    print("B")
elif marks >= 40:
    print("C")
elif marks >= 33:
    print("D")
else:
    print("Fail")