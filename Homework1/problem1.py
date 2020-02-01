# Author: Justin Trugman
# EE 605
# Homework 1, Problem 1


# Problem
# How many people do we need to have in a room to make it that the probability
# of two people in the room will have the same birthday is greater than ½? (Note: Here
# we consider just the day and month, not the year.)

# Answer = 23 people

if __name__ == "__main__":
    prob_no_match = 1
    days_in_year = 365
    counter = 0

    while prob_no_match > 0.5:
        prob_no_match = prob_no_match * (days_in_year/365)
        days_in_year = days_in_year - 1
        counter = counter + 1
        
    print("Probability of No Match = " + str(prob_no_match) + '\n')
    print("People for greater than 50 percent chance of same birthday =  " + str(counter))


