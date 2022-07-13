# ELSE IF STATEMENTS

# dog_size = int(input("How heavy is your dog? "))
# if dog_size > 8:
#     print("That's a heavy dog")
# elif dog_size < 8:
#     print("That's a light dog")

"""
You're cooking a pizza and need to check that the
oven is at the right temperature

Write a program to:
1. Ask the user to input the temperature
2. Prints "The oven is too hot" if the temperature is over 200
3. Prints "The oven is too cold" if the temperature is under 150
4. Prints "The oven is at the perfect temperature" if the temperature is 180
5. Prints "The temperature is close enough" for any other temperature
"""

# user_temp = float(input("What is the temperature? "))
# temperature = user_temp
#
# if temperature > 200:
#     print("The oven is too hot!")
# elif temperature < 150:
#     print("The oven is too cold!")
# elif temperature == 180:
#     print("The oven is at the perfect temperature!")
# elif:
#     print("The temperature is close enough")

# RANDOM

import random
# built in library for random data
# random_integer = random.randint(1, 100)
# print(random_integer)

sides = int(input("How many sides does your dies have? "))
random_integer = random.randint(1, sides)
print(f"You rolled a {random_integer}")

"""
Comparison operators in Pythn:
==	Equal		
!=	Not equal	
>	Greater than
<	Less than	
>=	Greater than or equal to
<=	Less than or equal to
"""