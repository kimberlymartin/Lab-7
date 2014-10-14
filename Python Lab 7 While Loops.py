#25pt
number = 1
while number < 300:
    print number
    number = number + 2
    
#50pt
theList = ['hey',2,3,67,'python',5,100,'october',434,'tuesday',5,2,4]
index = 0
while index < len(theList):
    print theList[index]
    index = index + 1
    
#100pt
import random
rand = random.randint(0,50)
guess = False
while guess == False:
    print "Make your guess!"
    userGuess = int(raw_input())
    if userGuess == rand:
        print "You got it! The number was " + str(userGuess)
        guess = True
    else:
        if userGuess > rand:
            print "That was too high, try again."
        else:
            print "That was too low, try again."