import turtle # allows us to use the turtles library
wn = turtle.Screen() # Setup the window and its attributes
wn.bgcolor("white") # Change the background color
wn.title("Nsabimana & Monica") # Make a title
Nsabimana= turtle.Turtle()
Nsabimana.color("red")
Nsabimana.penup()
Nsabimana.forward(-200)
Nsabimana.pendown()
Nsabimana.left(90)
Nsabimana.forward(200)
Nsabimana.right(135)
Nsabimana.forward(280)
Nsabimana.left(135)
Nsabimana.forward(200)


Steve= turtle.Turtle()
Steve.penup()
Steve.forward(100)
Steve.pendown()
Steve.color("blue")
Steve.circle(50,180)
Steve.circle(-50,180)

wn.exitonclick()
