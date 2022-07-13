import random

# colours = [
#     "pink",
#     "blue",
#     "purple",
#     "red",
#     "pink",
#     "green",
#     "orange"
# ]

# choose_colour = random.choice(colours)
# print(choose_colour)

"""
Write a program to create a random name. You should have a list
of random first-names and a list of last-names. 
Choose a random item from each and display the result

Extension: Using list of verbs and a list of nouns, create 
randomised sentences
"""

firstnames = ["Jimbo", "Chad", "Huckleberry", "Teeteee", "Winston", "Dicman", "Missymee", "Dennis", "Chad", "Snocky", "Figgy", "Butterbean", "Greasy", "Soupy", "Chewy"]
lastnames = ["BigMeat", "Henderson","Moonshine", "Rubbins", "Beetrootlover", "Stevens", "Clutterbuck", "Kingfish", "Fishhandler", "Whiplash", "Gobbler", "Swordbanger"]
verbs = ["breaking", "colouring", "crying", "drinking", "building", "coughing", "dancing", "eating", "coaching", "completing", "drawing", "entering"]
nouns = ["affair", "action", "disgust", "disease", "join", "interest", "kiss", "kick", "desire"]

firstname = random.choice(firstnames)
lastname = random.choice(lastnames)
verb = random.choice(verbs)
noun = random.choice(nouns)

sentence = "{} {} {} {}".format(firstname, lastname, verb, noun)

print(sentence)
