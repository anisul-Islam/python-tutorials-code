# Dictionaries -> key, value
# name -anisul islam
# email - anisul2010s@yahoo.co.uk
# word - meaning

studentId = {
    # "101" : "Anisul Islam",
    # "102": "Junaed Ahmed",
    # "103": "Rabeya Begum",
    101: "Anisul Islam",
    102: "Junaed Ahmed",
    103: "Rabeya Begum",
}

print(studentId[101])
# print(studentId.get("101"))
print(studentId.get(106, "Not a valid key"))
print(studentId.get(103, "Not a valid key"))