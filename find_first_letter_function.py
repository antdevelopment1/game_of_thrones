# Imports text file that we want to retireve infornmation from.
from characters import characters 

# Find all the names that begin with any letter.
# Creates a function that takes a parameter.
def start_with_a(letter):   

    # Holds value for number of times letter is the first characters in name's value.   
    count = 0  

    # For each dictionary in the characters list.                 
    for diction in characters:  

        # If the first index of the name in each dictionary matches letter passed in function...
        if diction['name'][0] == letter: 

            # we increment by 1.
            count += 1

            # Prints everyones name who begins with letter passed in function.
            print(diction['name']) 
    # Prints the count and letter passed in function.
    print("There are %d people whose names start with the letter %s " % (count, letter))

# Excecutes function and passes a prompt to ask for a letter value and converts it to uppercase.
start_with_a(input("Please choose a letter:").upper()) 
