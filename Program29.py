# tuples -> is a data structure like list but its value is not changeable (immutable)
# tuples is faster than list
students = (
    "Anisul Islam",
    "Rabeya Begum",
    "Anwar Alam",
)

print(students)
print(students[0])

# value can not be changed
# students[0] = "Misti"

# nested touples
studentsDetails = (
    ("Name : Anisul Islam", "ID : 101", "Age : 30"),
    ("Name : Rabeya Begum", "ID : 102", "Age : 29"),
    ("Name : Rokibul Islam", "ID : 103", "Age : 30"),
)
print(studentsDetails)
print(studentsDetails[0])
print(studentsDetails[1:])
