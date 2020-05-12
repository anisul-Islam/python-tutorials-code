# How to read in a file

# step 1 : open a file
# read mode -> r, write -> w, read and write -> r+
file = open("student.txt", "r")

# checking a file is readable or not
print(file.readable())
print(file.writable())

# reading the text from a a file
text = file.read()
print(text)

size = len(text)
print(size)

lines = file.readlines()
# lines = file.readlines() [0]
print(lines)



# always remember to close file at the end
file.close()