# A program to demonstrate List
subjects = ["C", "C++", "Java", "JavaScript", "Python"]
print(subjects)

# printing first element; index always start with 0
print(subjects[0])

# printing all the elements starting from index 1
print(subjects[1:])

# printing the last element
print(subjects[-1])

# check an element exist or not
print("Python" in subjects)
print("python" in subjects)
print("react" not in subjects)

# can multiple elements by any number
print(subjects*2)

# list related functions
# length of a list
print("Length of student list : " , len(subjects))

# checking the position of an item
pos = subjects.index("Java")
print("Position of java in subjects : ", pos)

# adding items at the end of a list
subjects.append("php")
print("After appending : ", subjects)

# remove the last item of a list
subjects.pop()
print("Removing the last element : ", subjects)

# inserting an item in list
subjects.insert(3,"Database")
print("After inserting : ", subjects)

# removing an item
subjects.remove("Java")
print("After removing : ",subjects)

# sorting a list
subjects.sort()
print("After sorting : ", subjects)

numbers = [2,45,10,20,40,5,45]
numbers.sort()
print("Sorting numbers in ascending orders : ",numbers)

numbers.reverse()
print("Sorting numbers in descending orders : ",numbers)

# clear the list
subjects.clear()
print("After clearing the list : ", subjects)

# copy one list to another
numbers2 = numbers.copy()
print("numbers2 = ", numbers2)

# count the appearance of an item
x = numbers.count(45)
print(x)

