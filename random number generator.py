#random number generator w/ 2 different number hugh and low and choose between them
import random

print("This program accepts two numbers given by the user and randomly produces a value within that range.")

low=int(input( "LOWER NUMBER IN YOUR RANGE:" ))
high=int(input( "HIGHER NUMBER IN YOUR RANGE:" ))

num = random.randint(low,high)

print(f"The randomly generated number is: {num}" )

#put in cmd: 
#$ cd starter 
#$python rng.py
