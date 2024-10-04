#random number generator w/ 2 different number hugh and low and choose between them
import random

print("This program intakes two numbers and randomly generates a number between them")

low=int(input( "LOWER NUMBER IN YOUR RANGE:" ))
high=int(input( "HIGHER NUMBER IN YOUR RANGE:" ))

num = random.randint(low,high)

print(f"The randomly generated number is: {num}" )

#put in cmd: 
#$ cd starter 
#$python rng.py
