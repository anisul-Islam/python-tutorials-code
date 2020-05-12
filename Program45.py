# swapping -> exchanging values of 2 variables
a = 20
b = 10
print(f"Before swapping a = {a}, b = {b}")

# swapping using extra variable
print("swapping using extra variable.", end=" ")
temp = a
a = b
b = temp
print(f"After swapping a = {a}, b = {b}")

# swapping without using extra variable
print("swapping without using extra variable.", end=" ")
a, b = b, a
print(f"After swapping a = {a}, b = {b}")