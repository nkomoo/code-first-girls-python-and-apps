"""

Rewrite this code to use a loop for and the range() function

print("~" * 0)
print("~" * 1)
print("~" * 2)
print("~" * 3)
print("~" * 4)
print("~" * 5)
print("~" * 6)
print("~" * 7)
print("~" * 8)

"""

for i in range(9):
    print("~" * i)

# COMPARISONS AND LOGICAL OPERATORS

"""
Boolean = a data-type that is either true or false, on or off
comparison operator = compare values to find out whether there is something true or false
"""

# This code checks if the user has input 'Monday' using the == operator
# If anything other than Monday it will be a false
today = input("What day is it today? ")
is_monday = today == "Monday"
print(f"Today is Monday: {is_monday}")



