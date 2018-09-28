# Imports characters.py file.
from characters import characters

# Creates function checking for season numbers.
def still_on_show():

    # Count represents # of people no longer on show.
    off_show_count = 0

    # Loops through each person's dictionary in characters.
    for person_diction in characters:

        # If the string 'Season 6' appears anywhere in the current dictionaries 'tvSeries' value...
        # If character possibly died during Season six...
        if "Season 6" not in person_diction['tvSeries'] or person_diction['died'] != "":

            # Increment count + 1.
            off_show_count += 1

    # Returns count of number of people no longer on show.
    return(" %d people are no longer on the show." % off_show_count)

# Saves function and invocation inside variable.
on_show = still_on_show()

# Prints and calls function.
print(on_show)




# for diction in characters[0].keys(): 
#     print(diction)