# List as input from user

# text = input("Enter a sentence : ")
# words = text.split()
# for word in words:
#     print(word)


numOfLetters = 0
numOfWords = 0
numOfDigits = 0

text = input("Enter a sentence : ")
for x in text:
    x = x.lower()
    if 'a' <= x <= 'z':
        numOfLetters += 1
    elif '0' <= x <= '9':
        numOfDigits += 1
    elif x == ' ':
        numOfWords += 1

print("Number of words = ", numOfWords + 1)
print("Number of letters = ", numOfLetters)
print("Number of digits = ", numOfDigits)