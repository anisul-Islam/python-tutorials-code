# xargs -> receive any number of parameters -> acts like tuples
def student(*details):
    print(details)
    print(details[1])


student(101, "Anisul Islam")
student(101, "Rokibul Islam", 3.92)

# xxargs -> receive any number of parameters -> acts like dictionaries -> key, value
def studentDetails(**details):
    print(details)
    print(details["id"])


studentDetails(id= 101,Name = "Anisul Islam")