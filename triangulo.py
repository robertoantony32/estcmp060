import turtle

# Screen() method to get screen
window = turtle.Screen()

# creating pen object
pen = turtle.Turtle()


def triangle(x, y):
    # it is used to draw out the pen
    pen.penup()

    # it is used to move cursor at x
    # and y position
    pen.goto(x, y)

    # it is used to draw in the pen
    pen.pendown()
    for i in range(3):
        # move cursor 100 unit
        # digit forward
        pen.forward(100)

        # turn cursor 120 degree left
        pen.left(120)

        # Again,move cursor 100 unit
        # digit forward
        pen.forward(100)


# special built in function to send current
# position of cursor to triangle
turtle.onscreenclick(triangle, 1)

turtle.listen()

# hold the screen
turtle.done()
