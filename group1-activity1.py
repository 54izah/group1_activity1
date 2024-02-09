'''
Done by: Group 1
Title: Activity 1 - Turtle-Drawing pattern
 
Al Tajer, Bachar
Hassan, Ahmed 
Faizah Mehek

CONTRIBUTION:
Bachar - CIRCLE FUNCTION, PATTERN FUNCTION
Ahmed - HEXAGON FUNCTION, MAIN FUNCTION
Faizah - SQUARE FUNCTION, SETPOS FUNCTION

This program uses the Turtle graphics library to draw a pattern consisting of squares, circles, and hexagons.
The user is prompted to input colors for shape borders, squares, circles, and hexagons.

Functions:
- setPos(turta, x, y): Set the turtle position and initialize the drawing environment.
- square(turta, square_color, pen_color): Draw a square with specified colors.
- circle(turta, circle_color, pen_color): Draw a circle with specified colors.
- hexagon(turta, hexagon_color, pen_color): Draw a hexagon with specified colors.
- pattern(): Create the pattern by calling the above functions.
- main(): Entry point of the program, calls the pattern function.
'''

import turtle 

x=150
y=-200

# Function to set the turtle position and initialize the drawing environment
def setPos(turta,x,y):
    turta=turtle
    turta.bgcolor("light blue")
    turta.up()
    turta.goto(x,y)
    turta.down()

# Function to draw a square
def square(turta,square_color,pen_color):
    turta=turtle
    turta.pensize(2)
    turta.pencolor(pen_color)
    turta.fillcolor(square_color)
    turta.begin_fill()
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.end_fill()
    turta.setheading(180)

# Function to draw a circle
def circle(turta, circle_color,pen_color):
    turta=turtle
    turta.up()
    turta.forward(90)
    turta.setheading(0)
    turta.down()
    turta.pencolor(pen_color)
    turta.fillcolor(circle_color)
    turta.begin_fill()
    turta.circle(50)
    turta.end_fill()

# Function to draw a hexagon
def hexagon(turta,hexagon_color,pen_color):
    turta=turtle
    turta.pencolor(pen_color)
    turta.up()
    turta.setheading(180)
    turta.forward(160)
    turta.setheading(0)
    turta.down()
    turta.fillcolor(hexagon_color)
    turta.begin_fill()
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.setheading(180)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.end_fill()
   
    

 # Function to create the pattern   
def pattern():
    turta=turtle
    borders_color=str(input("enter the color of the shape borders:"))
    square_color=str(input("enter the color of square:"))
    circle_color=str(input("enter the color of circle:"))
    hexagon_color=str(input("enter the color of hexagon:"))

    setPos(turta,x,y)
    turta.tracer(False)

    # Draw the first set of shapes
    square(turta,square_color,borders_color)
    circle(turta,circle_color,borders_color)
    hexagon(turta,hexagon_color,borders_color)

    # Move to the next position
    turta.setheading(90)
    turta.up()
    turta.forward(130)
    turta.setheading(0)
    turta.forward(150)
    turta.setheading(0)
    turta.down()

     # Draw the second set of shapes
    square(turta,square_color,borders_color)
    circle(turta,circle_color,borders_color)
    hexagon(turta,hexagon_color,borders_color)

    # Move to the next position
    turta.setheading(90)
    turta.up()
    turta.forward(130)
    turta.setheading(0)
    turta.forward(150)
    turta.setheading(0)
    turta.down()

    # Draw the third set of shapes
    square(turta,square_color,borders_color)
    circle(turta,circle_color,borders_color)
    hexagon(turta,hexagon_color,borders_color)


    turta.tracer(True)
    turta.done()

def main():
    pattern()
    
main()