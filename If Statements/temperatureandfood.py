# temperature = input("What is the temperature? ")
# its_freezing = float(temperature) <= 0.0 #temperatures are mostly float
# print(f"The temperature is freezing: {its_freezing}") #false or true

name = "Chantele"
person = name == "Sarah" #if changed to Chantele it will say True

print(person)

"""
You have a budget of £10 and want to write a program to decide
which burger restuarant to go to.

1. Input the price of a burger using input()
2. Check whether the pricess is less than or equal (<=) £10
3. Print the result in the format below

Burger is within budget: True

HINT: Remember to convert the input from a string to a 
decimal with float()
"""

# burger_price = input("What is the cost of the burger? ")
# its_cheap = float(burger_price) <= 10.00
# print(f"Burger is within budget: {its_cheap}")

"""
and = both expressions are true
or = at least one expression is true
not - reverse the expression (true becomes false and vice versa)
"""

"""
Add code to your burger program to input whether the restuarant 
has a vegetarian option.

The output should say whether the cost is within budget AND
has a vegetarian option

Restuarant meets criteria: True
"""

# burger_price = input("What is the cost of the burger? ")
# its_cheap = float(burger_price) <= 10.00
# print(f"Burger is within budget: {its_cheap}")
#
# veg_option = input("Does the restuarant have vegetarian options? [y/n] ")
# fits_criteria = veg_option == "y"
# print(f"Restuarant meets criteria: {fits_criteria}")

"""
Rewrite the output of your burger program to use if statements
"""

# if its_cheap and fits_criteria:
#     print("This restuarant is a great choice!")
# if not its_cheap or not fits_criteria:
#     print("Probably not a good idea!")

"""
Write a program to calculate your meal and apply a discount
if applicable

If your total meal costs more than $20 and you have a discount,
the price will be reduced by 10%. 

The program should print: "Discount Applied" or "No Discount.
If discount criteria was met

"""

meal_price = float(input("How much did the meal cost? "))
discount_choice = input("Do you have a discount? [y/n] ")
discount_applicable = discount_choice == "y"

if discount_applicable:
    meal_price = meal_price * 0.9
    print("Discount applied")
else:
    print("No discount")

print(f"Total cost: {meal_price}")




