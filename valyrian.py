# Imports character from character.
from characters import characters

# Creates a function.
def culture_of_char():

    # Creates a count to keep track of Valyrian culture.
    count = 0

    # Loops through each dictionary in character.
    for diction in characters:

        # Assings current dictionaries keys value to the variable culture.
        culture = diction['culture']

        # If the value of the dictionary's key equals Valyrian...
        if culture == 'Valyrian':

            # Count is incremented by 1.
            count += 1
    # Returns the number of people with a Valyrian background.
    return ("The are %d people with Valyrians culture." % count)

# Prints and calls function.
print(culture_of_char())