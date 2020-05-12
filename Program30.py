# set  -> an unordered collection of items.
# duplicate value will be automatically removed
# 2 ways to create set > set() , {}
set1 = {1, 2, 3, 4, 5, 5 , 5 }
print(type(set1))
print(set1)

set2 = set([4,2,3,6])
print(set2)

set2.add(7)
print(set2)

set2.remove(2)
print(set2)

# check an item is exist in a set
print(7 in set2)
print(7 not in set2)

# set operations
A = set([1,2,3,4])
B = set([4,5,6,7])

# UNION of 2 sets
print(A | B)

# Intersections of 2 sets
print(A & B)

# Differences  of 2 sets
print(A - B)