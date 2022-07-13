import turtle

turtle.speed(0)

# grass
turtle.bgcolor("green")


# sky
turtle.penup()
turtle.goto(-400,-100) #x = left y = down coordinates
turtle.pendown() #once in the coordinates we need put down

turtle.color("skyblue")
turtle.begin_fill() #fill in shape we draw

for line in range(2):
    turtle.forward(800) #800 pixels wide
    turtle.left(90)
    turtle.forward(500) #top of the page
    turtle.left(90)

turtle.end_fill()

# sun
turtle.penup()
turtle.goto(-220, 170)
turtle.pendown()
turtle.color("yellow")

turtle.begin_fill()
turtle.circle(40) #radius 35 pixels
turtle.end_fill()

# first cloud
turtle.penup()
turtle.goto(200, 200)
turtle.pendown()
turtle.color("white", "white")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(220, 240) #this changes
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(230, 215) #this changes
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(180, 225) #this changes
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

# second cloud

turtle.penup()
turtle.goto(-50, 200)
turtle.pendown()
turtle.color("white", "white")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(-70, 210)
turtle.pendown()
turtle.color("white", "white")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(-30, 210)
turtle.pendown()
turtle.color("white", "white")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(-30, 200)
turtle.pendown()
turtle.color("white", "white")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

# x = +right -left
# y = +up -down

# house
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()
turtle.pensize(3)
turtle.color("black", "brown")
turtle.begin_fill()

for square in range(4):
    turtle.forward(210)
    turtle.left(90)

# chimney
turtle.end_fill()
turtle.penup()
turtle.goto(50, 130)
turtle.pendown()
turtle.color("firebrick")
turtle.begin_fill()

for rectangle in range(2):
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

turtle.end_fill()

# roof
turtle.penup()
turtle.goto(-100, 110)
turtle.pendown()
turtle.color("black", "red")
turtle.begin_fill()

# x = +right -left
# y = +up -down

for triangle in range(3):
    turtle.forward(210)
    turtle.left(120)

turtle.end_fill()

# window one
turtle.penup()
turtle.goto(-70,0)
turtle.pendown()
turtle.color("black", "white")
turtle.begin_fill()

for window in range(4):
    turtle.forward(50)
    turtle.left(90)

turtle.end_fill()

# window one horizontal line
turtle.penup()
turtle.goto(-70,25)
# x = +right -left
# y = +up -down
turtle.pendown()
turtle.color("black")
turtle.forward(50)

# window one vertical line
turtle.penup()
turtle.goto(-45, -1.6)
turtle.left(90)
# x = +right -left
# y = +up -down
turtle.pendown()
turtle.color("black")
turtle.forward(50)

# window two
turtle.penup()
turtle.goto(80,0)

turtle.pendown()
turtle.color("black", "white")
turtle.begin_fill()

for window in range(4):
    turtle.forward(50)
    turtle.left(90)

turtle.end_fill()

# window two horizontal line
turtle.penup()
turtle.goto(55,0)
# x = +right -left
# y = +up -down
turtle.pendown()
turtle.color("black")
turtle.forward(50)

# window two vertical line

turtle.penup()
turtle.goto(80, 25)
turtle.left(90)
# x = +right -left
# y = +up -down
turtle.pendown()
turtle.color("black")
turtle.forward(50)

# door
turtle.penup()
turtle.goto(30, -97)
turtle.pendown()
turtle.right(90)
turtle.color("black", "white")
turtle.begin_fill()

for door in range(4):
    turtle.forward(50)
    turtle.left(90)

turtle.end_fill()

turtle.done()