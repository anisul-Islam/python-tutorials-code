# Matrix is a 2 dimensional array or list
A = [
    [1, 2, 3],
    [4, 5, 6]
]

# printing a specific element of a matrix
print(A[0][1])

# setting value of a matrix element
A[0] [1] = 20

# printing all the rows of a matrix
for row in A:
    print(row)

# printing each item of a matrix separately
for row in A:
    for col in row:
        print(col)