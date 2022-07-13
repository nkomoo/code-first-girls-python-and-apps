"""
programming language = language with a set of
rules used to communicate instructions
program: set of instructions run by a computer
"""

"""
python is:
-readable
-wide selection of 3rd party libraries
-popular
-open source
"""

"""
github is an open source
"""

print("Hello, World!")  #prints out Hello World

"""
function = reusable code that completes a tasks like print()
"""

print("How are you?")  #print() function used to ouput a message to the programmer
print("They\'re here")  #backslash to show that you do not want the code to end in the apostrophy in they're

# PUT THESE IN PYTHON CONSOLE

print(5-6)
print(8*9)
print(6/2)
# print(5/0)  #python cannot handle infinite numbers, as they are hard to write in concrete form so you get an error.
print(5%2)  #remainder/modulo
print(2*(10+3)) #bodmas/bidmas
print(2**4)  #2 to the power of 4

"""
python file: 
-runs all lines from top-to-bottom
-only shows when using print()
-for code that will run multiple times
python console:
-runs one line as it is written
-shows output for every line
-interactive for exploration
"""

# THE STRING DATA TYPE

print("Jane's")
print("cat")
print("cat " + "videos")  #merges words together
print("cat" * 3)  #says cat 3 times
# print("cat" + 3)  #error not in quotations can't add string and integers together
print("cat" + "3")  #string is a string and can put them together
print("cat".upper)  #uppercase
print("cat".lower)  #loweracse
print("lord of the rings".title)  #capitalise first letter of each word

"""
method = piece of code that completes a task for specific data-type
like .upper(), acn only be used with a string not an integer or float
"""

print("Cat " + str(3))  #convert a number to a string

# VARIABLES
"""
variables = reusuable label for a data value in python
assigning a variable in 3 parts:
-variables name
-an equals sign 
-data value it references
"""

username = "chantele"
age = 23
print(username, age)

# print("spaghetti")  #do below, reference variable

favourite_food = "spaghetti"
print(favourite_food)
