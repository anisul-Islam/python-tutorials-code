# List comprehensions

# finding square without using comprehension list
num = [1,2,3,4,5]
result = list(map(lambda x: x*x, num))
print(result)

# finding square  using comprehension list
# [expression for item in list]
result2 = [x*x for x in num]
print(result2)

# result3 = list(filter(lambda x : x%2==0, num))
result3 = [x for x in num if x%2==0]
print(result3)