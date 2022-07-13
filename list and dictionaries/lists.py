# LISTS

"""
Lists are written inside sqaure brackets and separated by commas
"""

# a list of integers
# lottery_num = [4,2,8,19]

# a list of strings
# student_names = ["chan","toby","violet"]

# lists can be made up of different data types
# person = ["jess", 32]

# list values can be accessed using index in square brackets
# student_names = ["Chan", "Bobby", "Girl"]
# print(student_names[2]) #will output student name Girl

# names = [
#     "Helena",
#     "Andre",
#     "Toby",
#     "Grace",
#     "Nina"
# ]
# names[1] = "Gemma" #changes Andre to Gemma
# print(names[1])

"""
Make a program to check if the first item in the clothes list is "shorts"
If it is it should change the value to "warm coat"
"""

# clothes = [
#     "shorts",
#     "shoes",
#     "t-shirt"
# ]

# clothes[0] = "warm coat"

# OR

# if clothes[0] == "shorts"
#     clothes[0] = "warm coat"

# print(clothes)

# LIST FUNCTIONS

"""
len() = number of items in a list
max() = the biggest value in a list
min() = smallest number in a list
"""

# costs = [1.2, 4.3, 2.0, 0.5]
#
# print(len(costs))
# print(max(costs))
# print(min(costs))

# numbers = [
#     5,
#     64,
#     8.9,
#     1.2,
#     -3
# ]

# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sorted(numbers)) #sorts number from lowest to highest
# print(list(reversed(numbers))) #lists revered order

# OR

# sort_number = sorted(numbers)
# print(list(reversed(sort_number)))

"""
Make a list of game scores. Using list functions write
code to output information of the scores in the following format: 

Number of scores: 10
Highest score: 200
Lowest score: 3

Extension: Output all of the scores in descending order
"""

numbers = [
    200,
    3,
    5,
    64,
    90,
    14,
    45,
    34,
    70,
    10
]

print(len(numbers))
print(max(numbers))
print(min(numbers))

sort_numbers = sorted(numbers)
print(sort_numbers)
print(list(reversed(sort_numbers)))
