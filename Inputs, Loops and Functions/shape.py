import turtle

# turtle.speed("slowest") #for slow and fast = "fastest"
#
# turtle.forward(100) #moves forward by 100 pixels
# turtle.right(130) #turns/rotates in 130 angle/direction
#
# turtle.done() #finished with the code

# DRAW A SQUARE (90 angle and wide by 100

side_length = 100
angle = 90

turtle.color("black", "green") #black outline and green fill
turtle.begin_fill() #begins to fill the shape with the colors

turtle.speed("fastest")

# turtle.forward(100)
# turtle.right(90)

# turtle.forward(100)
# turtle.right(90)

# turtle.forward(100)
# turtle.right(90)

# turtle.forward(100)
# turtle.right(90)

# OR ADDING VARIABLES

turtle.forward(side_length)
turtle.right(angle)

turtle.forward(side_length)
turtle.right(angle)

turtle.forward(side_length)
turtle.right(angle)

turtle.forward(side_length)
turtle.right(angle)

turtle.end_fill() #stops using the colors

turtle.done()