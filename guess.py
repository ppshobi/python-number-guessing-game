#!/usr/bin/python3

import random

secret=random.randint(1,10)

for guesstaken in range(1,7):
	print("Take a Guess!")
	guess=int(input())
	if(guess<secret):
		print("Your Guess is low")
	elif(guess>secret):
		print("Your Guess is high")
	else:
		break

if(guess==secret):
	print("Your Guess is correct" + str(guess))
	print("You Took "+str(guesstaken) +" Guesses")
else:
	print("You Took "+str(guesstaken) +" Guesses")
	print("The Secret was "+ str(secret))
	

