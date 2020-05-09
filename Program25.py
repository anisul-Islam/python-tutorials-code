# A guessing game
# import random
from random import randint
'''
start
Input Guess Number
Generate Random number
If (guessNumber == randomNumber)
    i) yes, you have won
    ii) No, You have lost
end
'''

for x in range(1, 6):
    guessNumber = int(input("Enter your guess between 1 to 5 : "))
    randomNumber = randint(1,5)
    # randomNumber = random.random() * 100
    if guessNumber == randomNumber:
        print("You have won")
    else:
        print("You have lost.Random number was ",randomNumber)