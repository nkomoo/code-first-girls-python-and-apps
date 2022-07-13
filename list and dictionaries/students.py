# student_names = input("Which student are you looking for? ")

# students = [
#     "Chantele",
#     "David",
#     "Wayne",
#     "Lucas",
#     "Layla",
#     "Fatu",
#     "Sheriff"
# ]

# if student_names in students:
#     print(f"{student_names} is in the class!")
# else:
#     print(f"{student_names} is not in the class.")

# new_student = input("What is the name of the new student? ")

# students.append(new_student) #add a student to the list
# print(students)

# A method is an in-built function attached to a certain data type

"""
Create a list and if "bread" is in the list, add "butter"
to the shopping list.

Try running the program with and check that your program works

TIP: in operator checks if an item is in a list and the
.append() method adds an item to a list
"""

# shopping_list = [
#     "bread",
#     "sugar",
#     "fish",
#     "yoghurts",
#     "cheese"
# ]

# if "bread" in shopping_list:
#     shopping_list.append("butter")
#     print(shopping_list)

# if "bread" in shopping_list:
#     print("You forgot an ingredient!")

students = [
    "Diedre",
    "Hank",
    "Helena",
    "Salome"
]

count = 0

for name in students: #no range here as showed in other topisc
    # print(name)
    count = count + 1
print(count)

"""
Write a program that uses a for loop to calculate the total cost
"""

costs = [
    8.30,
    7.12,
    5.01,
    1.00,
    0.99,
    5.92,
    3.50
]

total = sum(costs)
print(total)


# print(round(total_cost))

# OR

# total_cost = 0
# for cost in costs:
#     total_cost = total_cost + cost
#     print(round(total_cost, 2))
