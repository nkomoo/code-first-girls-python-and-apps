#Draw a triangle with 3 sides and an angle of 120 degrees
import turtle

side = 100
angle = 120

turtle.color("black", "blue")
turtle.begin_fill()

turtle.forward(side)
turtle.right(angle)

turtle.forward(side)
turtle.right(angle)

turtle.forward(side)
turtle.right(angle)

turtle.end_fill()
turtle.done()

