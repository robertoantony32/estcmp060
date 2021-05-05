# Python program for Plotting Fibonacci
# spiral fractal using Turtle
import turtle
import math


def fibo_plot(number):
    a = 0
    b = 1
    square_a = a
    square_b = b

    # Setting the colour of the plotting pen to blue
    pen.pencolor("blue")

    # Drawing the first square
    pen.forward(b * factor)
    pen.left(90)
    pen.forward(b * factor)
    pen.left(90)
    pen.forward(b * factor)
    pen.left(90)
    pen.forward(b * factor)

    # Proceeding in the Fibonacci Series
    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    # Drawing the rest of the squares
    for _ in range(1, number):
        pen.backward(square_a * factor)
        pen.right(90)
        for _ in range(2):
            pen.forward(square_b * factor)
            pen.left(90)
        pen.forward(square_b * factor)

        # Proceeding in the Fibonacci Series
        temp = square_b
        square_b = square_b + square_a
        square_a = temp

    # Bringing the pen to starting point of the spiral plot
    pen.penup()
    pen.setposition(factor, 0)
    pen.seth(0)
    pen.pendown()

    # Setting the colour of the plotting pen to red
    pen.pencolor("red")

    # Fibonacci Spiral Plot
    pen.left(90)
    for _ in range(number):
        print(b)
        forward_distance_for_width = math.pi * b * factor/2
        forward_distance_for_width /= 90
        for _ in range(90):
            pen.forward(forward_distance_for_width)
            pen.left(1)
        temp = a
        a = b
        b = temp + b


# Here 'factor' signifies the multiplicative
# factor which expands or shrinks the scale
# of the plot by a certain factor.
factor = 1

# Taking Input for the number of
# Iterations our Algorithm will run
var = int(input('Enter the number of iterations (must be > 1): '))

# Plotting the Fibonacci Spiral Fractal
# and printing the corresponding Fibonacci Number
if var > 0:
    print("Fibonacci series for", var, "elements :")
    pen = turtle.Turtle()
    pen.speed(100)
    fibo_plot(var)
    turtle.done()
else:
    print("Number of iterations must be > 0")
