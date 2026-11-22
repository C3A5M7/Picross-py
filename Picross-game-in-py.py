from turtle import *
from time import *
from math import *
import keyboard
#5x5 grid with grid(5,5,150)

#size in 5x5 = 100*5px
#size in 10x10 = 50x10px
#size in 15x15 = 33x15px
#size in 20x20 = 25x20px
#size in 25x25 = 20x25px 

# all need to be 500 by 500 px


Picross_list=[[],]          #List of all curent picross
Solution_list=[]            #Current playing picross 
Player_list=[]              #Squares placed by player

def start_player_list(P_list,size):

    for i in range (size):
        P_list.append([])
        for i in range (size):
            P_list[-1].append(0)














def choose (picross_size):
    if picross_size == 5:
        grid(5,5,100)
    if picross_size == 10:
        grid(10,10,50)
    if picross_size == 15:
        grid(15,15,33)
    if picross_size == 20:
        grid(20,20,25)
    if picross_size == 25:
        grid(25,25,20)

def grid(rows,columns,size) : #set a grid of rows and columns with square 
    setheading(90)
    for a in range (columns+1):
        penup()
        goto(a*size,0)
        pendown()
        forward(size*(rows))
        pendown()

    setheading(0)
    for b in range (rows+1):
        penup()
        goto(0,b*size)
        pendown()
        forward(size*(columns))

def arrow(x,y,orientation,size):   #make an arrow of size of the block ex:  for box of 50x50px. arrow is 50 in size
    size=size/2
    size=sqrt(size*size+size*size)
    penup()
    goto(x,y)
    pendown()
    if orientation == 'down' :
        setheading(135)
        forward(size)
        forward(-size)
        setheading(45)
        forward(size)
        forward(-size)
    if orientation == 'right' :
        setheading(135)
        forward(size)
        forward(-size)
        setheading(225)
        forward(size)
        forward(-size)
    penup()


def square(x,y,size): #make a square of side length = size at x,y cordinate
    penup()
    goto(x,y)
    pendown()
    setheading(0)
    for i in range (4):
        forward(size)
        right(90)
    penup()


def cross (x,y,size): #draw a cross to show the cursor location on grid proportional to grid size
    penup()
    goto(x,y)
    setheading(135)
    forward ((size/2)*0.8)
    left(180)
    pendown()
    forward (size*0.8)
    penup()

    goto(x,y)
    setheading(45)
    forward ((size/2)*0.8)
    left(180)
    pendown()
    forward (size*0.8)

    

print("test")
speed(0)
""" for x in range (-400,400,150):  
    for y in range (-400,400,150):  
        penup()
        goto(x-5,y)
        pendown()
        setheading(0)
        forward(10)
        penup()
        goto(x,y-5)
        pendown()
        setheading(90)
        forward(10)
 """

def square (x,y,size,square_list,xlist,ylist):   #draw a square at coordinate to place a square on the picross
    penup()
    setheading(0)
    goto(x-size/2,y-size/2)
    pendown()
    begin_fill()
    for i in range (4):
        forward(size)
        left(90)
    end_fill()
    penup()
    if square_list[xlist][ylist]==1:
        square_list[xlist][ylist]=0


    else:
        square_list[xlist][ylist]=1
        

    



def control (size,square_list):

    if size == 5:   #give the number of px to move to be aligned with the grid and is also used in the arrow size
        move=100
    if size == 10:
        move=50
    if size == 15:
        move=33
    if size == 20:
        move=25
    if size == 25:
        move=20

    cursor_row=move/2           #set the starting position of the arrows
    cursor_column=move/2+(move*size)-move

    xlistpos=0      #position in the player list
    ylistpos=0




    tracer(0,0)         #show the screen
    choose(size)
    arrow(cursor_row,500,'down',move)
    arrow(0,cursor_column,'right',move)
    cross(cursor_row,cursor_column,move)
    tracer(1,0)

    while True:
        if keyboard.is_pressed('up'):
            cursor_column=cursor_column+move
            clearscreen()
            tracer(0,0)
            choose(size)
            arrow(cursor_row,500,'down',move)
            arrow(0,cursor_column,'right',move)
            cross(cursor_row,cursor_column,move)
            ylistpos-=1
            tracer(1,0)
            sleep(0.1)
            print(cursor_column,cursor_row)

        elif keyboard.is_pressed('down'):
            cursor_column=cursor_column-move
            clearscreen()
            tracer(0,0)
            choose(size)
            arrow(cursor_row,500,'down',move)
            arrow(0,cursor_column,'right',move)
            cross(cursor_row,cursor_column,move)
            ylistpos+=1
            tracer(1,0)
            sleep(0.1)
            print(cursor_column,cursor_row)

        elif keyboard.is_pressed('right'):
            cursor_row=cursor_row+move
            clearscreen()
            tracer(0,0)
            choose(size)
            arrow(cursor_row,500,'down',move)
            arrow(0,cursor_column,'right',move)
            cross(cursor_row,cursor_column,move)
            xlistpos+=1
            tracer(1,0)
            sleep(0.1)
            print(cursor_column,cursor_row)

        elif keyboard.is_pressed('left'):
            cursor_row=cursor_row-move
            clearscreen()
            tracer(0,0)
            choose(size)
            arrow(cursor_row,500,'down',move)
            arrow(0,cursor_column,'right',move)
            cross(cursor_row,cursor_column,move)
            xlistpos-=1
            tracer(1,0)
            sleep(0.1)
            print(cursor_column,cursor_row)

        elif keyboard.is_pressed('c'):
            clearscreen()
            tracer(0,0)
            choose(size)
            arrow(cursor_row,500,'down',move)
            arrow(0,cursor_column,'right',move)
            square(cursor_row,cursor_column,move,square_list,xlistpos,ylistpos)
            cross(cursor_row,cursor_column,move)
            tracer(1,0)
            sleep(0.1)
            print(cursor_column,cursor_row)

        
        print(xlistpos,ylistpos)
        sleep(0.01)

        
        



control(5,Player_list)

        