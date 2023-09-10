# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 18:07:19 2023

@author: Bravender
"""


import random
random_number = random.randint(1, 100)
round_number = 1

def main(round_number):
    while True:
        try:
            #The user makes a guess, and the try/except block ensures it is a valid input
            user_input = int(input("Guess the number from 1 to 100: "))
            if user_input > 100 or user_input < 1: 
                print("Invalid input")
                continue
        except ValueError:
            print("Invalid input")
            continue
        
        # we calculate the difference between what the guess was, and what the number is 
        # we can than use this variable "differnce" to see if they need to guess higher or lower
        difference = user_input - random_number
            
        
    # if they guessed a number too high
        if difference > 0:
           # Down Arrow
           print("↓")
    # if they guessed a number too low    
        elif difference < 0:
            # Up Arrow
            print("↑")
        # if their input is the same as the number
        else:
            print("Good Job!! You got it in " + str(round_number) + " guesses!" )
            break
        
        round_number+= 1
    
   
# Start the game by calling the main function
# Ensures that the code only recalls the main function currently being run as opposed to another function named main
if __name__ == "__main__":
    main(round_number)



