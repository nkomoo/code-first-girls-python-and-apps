# LOOPS
"""
For loop = lets you repeat a block of code multiple times
A for loop has:
-for operator
-variable name that stores each list value one at a time
-in operator
-collection of values
-a body (indented four spaces)
"""

# for number in range(101):
#     print(number)

# SHAPES OF SQUARE IN A 4 LOOP
import turtle

# side = 100
# angle = 90

# turtle.color("black", "green")
# turtle.begin_fill()

# turtle.speed("fastest")

# for line in range(4):
#     turtle.forward(side)
#     turtle.right(angle)

# turtle.end_fill()
# turtle.done()

# DRAW A PROGRAM THAT CAN DRAW SHAPES WITH ANY NUMBER OF SIDES

# sides = int(input("Number of sides: "))

# angle = 90
# side_length = 100

# OR

# angle = 360 / sides
# side_length = 60

# for side in range(sides):
#     turtle.forward(side_length)
#     turtle.right(angle)

# turtle.done()

# FUNCTIONS
"""
function = reusuable block of code
All functions have:
-def operator
-a name
-brackets
-a colon
-body (indented 4 spaces)
"""

turtle.color("blue", "cyan")
turtle.begin_fill()

# def square():
#     side_length = 100
#     angle = 90

# OR

def square(side_length, colour):
    angle = 90

    turtle.color(colour, colour)
    turtle.begin_fill()

    for line in range(4):
        turtle.forward(side_length)
        turtle.right(angle)

# square() #to make something happen i.e. draw the square with color
# turtle.forward(100) #draw another square next to each other
# code below makes 3 squares
square(300,"red")
square(200, "blue")
square(100, "green")

turtle.end_fill()

turtle.done()
