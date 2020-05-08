# sum of n numbers using while loop
# 1 + 2 + 3 + ... + n
sum = 0
i = 1
n = int(input("Enter the last number : "))
while i <= n:
    sum = sum + i
    i = i + 1
print("sum = ", sum)


# 2 + 4 + 6 + ... + n
sum = 0
i = 2
n = int(input("Enter the last number : "))
while i <= n:
    sum = sum + i
    i = i + 2
print("sum = ", sum)