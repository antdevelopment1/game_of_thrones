# Import file from characters.
from characters import characters

# Creats title function.
def titles():
    
    # Creates an empty dictionary to store the number of titles.
    title_lengths = []

    # Loops through each dictionary in the characters file.
    for diction in characters:

        # Store the lenth of the number of titles for each dictionary.
        number_of_titles = len(diction['titles'])

        # Adds the legnth of each title for each dictionary into title_lengths list.
        title_lengths.append(number_of_titles)

        # Assigns the largest number in list to record_for_most_titles.
        record_for_most_titles = max(title_lengths)

    # Prints the highest value in list above.
    print(record_for_most_titles)

    # Finds the index of the dictionary associated with the the largest value in the title_lengths list.
    index_of_person = title_lengths.index(record_for_most_titles)

    # Prints the index for the person who has 7 titles.
    print(index_of_person)

    # Finds the character inside the list with the 1 index.
    person_with_most_titles = characters[index_of_person]

    # The index above allows us to print characters[1]['name] essentially.
    print(person_with_most_titles['name'] + " has the most titles.")

# Calls function.
titles()
