num_of_oranges = 12
cost_per_orange = 0.6

#total cost of 12 oranges?
print(int(num_of_oranges * cost_per_orange))  #integer
print(num_of_oranges * cost_per_orange) #float

#OR

total_cost = num_of_oranges * cost_per_orange
print(str(num_of_oranges) + " oranges costs " + str(int(total_cost))) #adds an integer
print(str(num_of_oranges) + " oranges costs " + str(float(total_cost))) #adds a float

#OR

orange_msg2 = f'{num_of_oranges} oranges cost £{total_cost:.2f}' #2 decimal place = .2f
print(orange_msg2)

# DATA TYPES

# type() #finds out the data type for you
print(type(12)) #is an integer
print(type(12.5)) #is a float
print(type("Jane")) #is a string

# STARTER (mistakes in the following code)
# name = Jess #no quotation marks as it is a string
# age = 20
# print(f'My name is {} and l am {} years old') #variables not in the {} in the format method