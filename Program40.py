# Recursion -> calling a function itself. 2 important things -> recursive call, base case for stopping
def fact(n):
    if n == 1:
        return 1

    return n * fact(n-1)


print(fact(5))