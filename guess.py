#!/usr/bin/python3
#Guessing game -Shobi  P P
#Simple number Guessing Game for beginners

import random
secret=random.randint(1,10)
print("**********************")
print("Number Guessing Game")
print("**********************")
print("Give me Your Name")
name=input()
print("Welcome "+ name)
for guesstaken in range(1,6):
	print("\nTake a Guess! "+ name)
	guess=int(input())
	if(guess<secret):
		print("Your Guess is low!")
	elif(guess>secret):
		print("Your Guess is high!")
	else:
		break

if(guess==secret):
	print("***********You Win***********")
	print("Your Guess is correct " + str(guess))
	print("You Took "+str(guesstaken) +" Guesses")
else:
	print("***********You Lose**********")
	print("You Took "+str(guesstaken) +" Guesses")
	print("The Secret was "+ str(secret))
	

