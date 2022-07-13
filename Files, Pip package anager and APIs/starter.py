"""
Starter: How do l ouput the species values for each of the dictionaries?
"""

# names = [
#     {"species": "zebra", "name": "Penelope"},
#     {"species": "penguin", "name": "Jenn"},
#     {"species": "elephant", "name": "Harris"},
#     {"species": "flamingo", "name": "Florence"},
#
# ]

# for animals in names:
#     print(animals['species'])

# READING/WRITING FILES

# Writing to a file
# with open("people.txt", "w+") #the name of the file, w+ means putting the computer in write mode
#     people = "Joanne \nSusan \nAmina" #backslash n means you want a new line

    # text_file.write(people)

# We can write on files (write mode)
with open("people.txt", "w+") as text_file:
    people = "Joanne \nSusan \nAmina"

    text_file.write(people)

# We can read files (read mode)
with open("people.txt", "r") as text_file:
    contents = text_file.read()

print(contents)

# r+ means we can read and write a file
# a is append mode (write a file and append more info)
# a+ append and read mode without overwriting anything
# x exclusive creating mode, creates a new file (doesnt have to exist before hand)

