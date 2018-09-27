# Imports characters file.
from characters import characters

# Defines/creates a function.
def find_hot_pie():

    # Loops through each dictionary in characters.
    for diction in characters:

            # Checks if the current dictionaries values is "Hot Pie".
            if diction['name'] == "Hot Pie":

                # If it is then we also print the current value of who plays that part in the current dictionary.
                return "Yay %s, also known as %s has been found!!!" % (diction['playedBy'][0], diction['name'])

                # Once we find "Hot Pie" we break out of the loop. No need to keep looking for anything else.
                break
# Calls function
found = find_hot_pie()
print(found)