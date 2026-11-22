from turtle import *

def grid(rows,columns) : #set a grid of rows and columns
    pass


def square(x,y,size):
    penup()
    goto(x,y)
    pendown()
    setheading(0)
    for i in range (4):
        forward(size)
        right(90)
    penup()

print("test")