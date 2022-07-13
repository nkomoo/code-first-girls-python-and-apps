num_of_oranges = 12
cost_per_orange = 0.6

#total cost of 12 oranges?
print(int(num_of_oranges * cost_per_orange))  #integer
print(num_of_oranges * cost_per_orange) #float

#OR

total_cost= num_of_oranges * cost_per_orange
print(str(num_of_oranges) + " oranges costs " + str(int(total_cost))) #adds an integer
print(str(num_of_oranges) + " oranges costs " + str(float(total_cost))) #adds a float
