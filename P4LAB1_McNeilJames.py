# James McNeil
# 9/23/24
# P4LAB1
# Use turtle library to draw shapes with loops

# Import the turtle library for drawing
import turtle

# Create a window for turtle to draw in
window = turtle.Screen()

# Turtle a turtle object
tom = turtle.Turtle()

# For loop to draw a square
for side in range (4):
    tom.forward(150)
    tom.right(90)

# While loop to draw triangle
var = 0
while var < 3:
    tom.forward(150)
    tom.left(120)
    var = var + 1
print("Loop is broken, var equal", var)
