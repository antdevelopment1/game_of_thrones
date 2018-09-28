# Produce a list characters with the last name "Targaryen"
# Imports characters file.
from characters import characters

# Creates an empty list.
same_last_name = []

# Loops through each dictionary in characters file.
for diction in characters:

    # Assigns each keys value inside of each dictionary.
    full_name = diction['name']

    # Checks to see if Targaryen is in the value of the key 'name' inside of diction.
    if "Targaryen" in full_name:

        # Appends the value of the full name inside diction['name].
        same_last_name.append(full_name)
# Prints the new updated list.
print(same_last_name)
