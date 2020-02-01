# Author: Justin Trugman
# EE 605
# Homework 1, Problem 3


# Problem
# The number of triples of integers from 1 to 6 with sum 9 is the same as the
# number of such triples with sum 10. However, when three dice are rolled, a 9 seems to
# come up less often than a 10.

#   (a) Write a program to simulate the roll of three dice a large number of times and keep
#       track of the proportion of times that the sum is 9 and the proportion of times it is 10.
#   (b) Can you conclude from your simulations that the observation is correct?

# Answer = I can conclude from my simulations that the observation is correct
#   See example output below:
        # Number of Dice Rolls = 10000000
        # Number of 9s = 1158496
        # Number of 10s = 1248826
        # TRUE: 9s have come up LESS than 10s

import random

def roll_dice():
    return random.randint(1,6)

if __name__ == "__main__":
    number_of_rolls = 10000000
    count_nines = 0
    count_tens = 0
    
    i = 0
    while i < number_of_rolls:
        i = i + 1
        dice_sum = roll_dice() + roll_dice() + roll_dice() 
        if dice_sum == 9:
            count_nines = count_nines + 1
        elif dice_sum == 10:
            count_tens = count_tens + 1
        else:
            continue

    print("Number of Dice Rolls = " + str(number_of_rolls))
    print("Number of 9s = " + str(count_nines))
    print("Number of 10s = " + str(count_tens))

    if count_nines < count_tens:
        print("TRUE: 9s have come up LESS than 10s")
    else:
        print("FALSE: 9s have come up MORE than 10s")
