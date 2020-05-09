# pattern related program
'''
n = 4
*
**
***
****
'''

n = int(input("Enter n = "))
for x in range(1, n+1, 1):
    print(x*"*")

'''
n = 4
*
***
*****
*******
'''
n = int(input("Enter n = "))
for x in range(1, n+1, 1):
    print((2*x-1)*"*")