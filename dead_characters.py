# Imports text file that we want to retireve infornmation from.
from characters import characters 

# Find everyone who is dead.
# Creates a function that takes a parameter.
def is_dead():   

    # Holds value for number of dead people.   
    count = 0  

    # For each dictionary in the characters list.                 
    for diction in characters:  

        # If dead people != an empty string(empty because their alive) and died in the year 299, we know their dead.
        if diction['died'] != '' and '299' in diction['died']: 

            # we increment by 1.
            count += 1

    # Prints the count of dead people who died in 299.
    return "There are %d dead people that died in the year 299" % count

# Invokes/calls and prints function.
dead = is_dead()
print(dead)
