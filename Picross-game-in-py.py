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

size=5
Picross_list=[[[[1,0,1,0,1],
                [1,1,1,1,1],
                [0,1,0,1,0],
                [0,1,1,1,0],
                [1,1,1,1,1]],'Castle'],
                
              [[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
                [1,1,0,1,1,1,1,1,1,1,1,1,0,1,1],
                [1,1,0,1,1,0,0,0,0,0,1,1,0,1,1],
                [1,1,0,1,1,0,0,0,0,0,1,1,0,1,1],
                [1,1,0,1,1,0,0,0,0,0,1,1,0,1,1],
                [1,1,0,1,1,0,0,0,0,0,1,1,0,1,1],
                [1,1,0,1,1,1,1,1,1,1,1,1,0,1,1],
                [1,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
                [1,1,0,0,1,0,0,0,0,0,0,0,0,1,1],
                [1,1,0,1,1,1,0,0,0,0,0,0,0,1,1],
                [1,1,0,0,1,0,0,0,0,1,1,1,0,1,1],
                [1,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
                [1,1,0,0,0,0,0,0,0,0,0,0,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],'Game Boy'],

              [[[1,0,1,0,0,1,1,1,1,0],
                [1,0,1,0,1,1,1,1,1,1],
                [1,1,1,0,1,1,0,0,1,1],
                [1,0,0,1,1,0,1,1,0,1],
                [1,0,0,1,1,0,0,1,0,1],
                [0,1,0,1,1,1,1,1,0,1],
                [0,1,0,0,1,0,0,0,1,1],
                [0,1,0,0,0,1,1,1,1,1],
                [0,0,1,0,0,0,0,0,0,0],
                [0,0,0,1,1,1,1,1,1,1]],'Snail'],

              [[[0,0,0,1,0,1,0,1,0,0],
                [0,0,0,1,0,1,0,1,0,1],
                [0,0,0,1,0,1,0,1,0,1],
                [0,0,0,1,0,1,0,1,0,1],
                [0,0,0,1,1,1,1,1,1,1],
                [1,1,0,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1],
                [0,1,1,1,1,1,1,1,1,1],
                [0,0,1,1,1,1,1,1,1,1],
                [0,0,0,1,1,1,1,1,1,0]],'Glove'],

              [[[0,0,0,0,1,1,0,0,0,0],
                [0,0,0,1,1,1,1,0,0,0],
                [0,0,0,1,1,1,1,0,0,0],
                [1,1,1,1,1,1,1,1,1,1],
                [1,1,0,1,1,1,1,1,1,1],
                [0,1,1,0,1,1,1,1,1,0],
                [0,0,1,0,1,1,1,1,0,0],
                [0,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,0,0,1,1,1,0],
                [1,1,1,0,0,0,0,1,1,1]],'Star'],

              [[[0,0,0,0,1,1,0,0,0,0],
                [0,0,0,1,1,1,1,0,0,0],
                [0,0,1,1,1,1,1,1,0,0],
                [0,1,1,1,1,1,1,1,1,0],
                [1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1],
                [0,1,1,0,1,1,0,1,1,0],
                [0,0,0,1,1,1,1,0,0,0],
                [0,0,1,1,1,1,1,1,0,0]],'Spike'],

              [[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
                [0,0,1,1,1,0,0,0,0,1,1,1,1,0,0],
                [0,1,1,0,0,0,0,0,0,1,1,1,1,1,0],
                [0,1,0,0,0,0,0,0,1,1,1,1,1,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [0,1,0,0,1,0,0,0,1,1,0,0,1,1,0],
                [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,1,1,1,1,1,1,1,1,1,1,1,0,0],
                [0,1,0,0,0,0,0,0,0,1,1,1,1,1,0],
                [0,1,0,0,0,0,0,0,1,1,1,1,1,1,0],
                [0,1,1,0,0,0,0,1,1,1,1,1,1,1,0],
                [0,0,1,1,1,1,1,1,1,1,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],'Burger'],

              [[[0,0,0,1,1,1,1,1,1,1,1,1,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,1,0,0,0,1,0,1,1,1,1],
                [1,1,1,1,0,1,0,0,0,1,0,1,1,1,1],
                [0,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
                [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0],
                [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
                [0,0,1,1,1,0,1,1,1,0,1,1,1,0,0],
                [0,0,1,1,1,0,1,1,1,0,1,1,1,0,0],
                [0,1,1,1,1,0,1,1,1,0,1,1,1,1,0],
                [0,1,1,1,1,1,0,0,0,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0]],'Phone'],

              [[[0,1,0,1,0],
                [0,0,0,0,0],
                [0,0,1,0,0],
                [1,0,0,0,1],
                [1,1,1,1,1]],'Face']]  #List of all curent picross  [LIST[Picross[rows0[Column0,Column1,ect]],Name]]
print(Picross_list[0][0])
Solution_list=[]            #Current playing picross 
Player_list=[]              #Squares placed by player

def start_player_list(size):
    P_list=[]
    for i in range (size):
        P_list.append([])
        for i in range (size):
            P_list[-1].append(0)
    return P_list


hideturtle()
Player_list=start_player_list(size)


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
    color('black')
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
    size=size/4
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
    color ('blue')
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

    
        
def show_square (size,square_list):   #draws squares on picross with the player_list

    if size == 5:   #give the number of px to move to be aligned with the grid 
        mult=100
    if size == 10:
        mult=50
    if size == 15:
        mult=33
    if size == 20:
        mult=25
    if size == 25:
        mult=20


    penup()
    setheading(0)
    for y in range (len(square_list[-1])):
        for x in range (len(square_list[-1])):
            if square_list[x][y]==1:
                color('black')
                goto(x*mult,-y*mult+((size-1)*mult))
                pendown()
                begin_fill()
                for i in range (4):
                    forward(mult)
                    left(90)
                end_fill()
                penup()
            else:
                color('white')
                goto(x*mult,-y*mult+((size-1)*mult))
                pendown()
                begin_fill()
                for i in range (4):
                    forward(mult)
                    left(90)
                end_fill()
                penup()
    color('black')
   
        
def Picross_selection(List):
    selected=0
    list_size=[]
    

    for i in range(len(List)):
        list_size.append(len(List[i][0]))



    tracer(0,0)
    grid(3,3,100)
    penup()
    goto(5,275)
    pendown()
    write("Picross 1", align="left", font=("Courier", 16, "bold"))
    penup()
    goto(5,225)
    pendown()
    write('5X5', align="left", font=("Courier", 16, "bold"))
    
    penup()
    goto(105,275)
    pendown()
    write("Picross 2", align="left", font=("Courier", 16, "bold"))
    penup()
    goto(105,225)
    pendown()
    write('15X15', align="left", font=("Courier", 16, "bold"))

    penup()
    goto(205,275)
    pendown()
    write("Picross 3", align="left", font=("Courier", 16, "bold"))
    penup()
    goto(205,225)
    pendown()
    write('10X10', align="left", font=("Courier", 16, "bold"))

    penup()
    goto(5,175)
    pendown()
    write("Picross 4", align="left", font=("Courier", 16, "bold"))
    penup()
    goto(5,125)
    pendown()
    write('10X10', align="left", font=("Courier", 16, "bold"))

    penup()
    goto(105,175)
    pendown()
    write("Picross 5", align="left", font=("Courier", 16, "bold"))
    penup()
    goto(105,125)
    pendown()
    write('10X10', align="left", font=("Courier", 16, "bold"))

    penup()
    goto(205,175)
    pendown()
    write("Picross 6", align="left", font=("Courier", 16, "bold"))
    penup()
    goto(205,125)
    pendown()
    write('10X10', align="left", font=("Courier", 16, "bold"))

    penup()
    goto(5,75)
    pendown()
    write("Picross 7", align="left", font=("Courier", 16, "bold"))
    penup()
    goto(5,25)
    pendown()
    write('15X15', align="left", font=("Courier", 16, "bold"))

    penup()
    goto(105,75)
    pendown()
    write("Picross 8", align="left", font=("Courier", 16, "bold"))
    penup()
    goto(105,25)
    pendown()
    write('15X15', align="left", font=("Courier", 16, "bold"))

    penup()
    goto(205,75)
    pendown()
    write("Picross 9", align="left", font=("Courier", 16, "bold"))
    penup()
    goto(205,25)
    pendown()
    write('5X5', align="left", font=("Courier", 16, "bold"))


    
    tracer(1,0)


    while selected==0:
        if keyboard.is_pressed('1'):
            selected=1
            size=5

        if keyboard.is_pressed('2'):
            selected=2
            size=15

        if keyboard.is_pressed('3'):
            selected=3
            size=10

        if keyboard.is_pressed('4'):
            selected=4
            size=10

        if keyboard.is_pressed('5'):
            selected=5
            size=10

        if keyboard.is_pressed('6'):
            selected=6
            size=10

        if keyboard.is_pressed('7'):
            selected=7
            size=15

        if keyboard.is_pressed('8'):
            selected=8
            size=15

        if keyboard.is_pressed('9'):
            selected=9
            size=5

    clearscreen()
    return(selected-1,size)

        



    



def control (size,square_list,Solve_list):

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
            arrow(cursor_row,500,'down',move)
            arrow(0,cursor_column,'right',move)
            show_square(size,square_list)
            cross(cursor_row,cursor_column,move)
            choose(size)
            ylistpos-=1
            tracer(1,0)
            sleep(0.1)
            print(cursor_column,cursor_row)

        elif keyboard.is_pressed('down'):
            cursor_column=cursor_column-move
            clearscreen()
            tracer(0,0)
            arrow(cursor_row,500,'down',move)
            arrow(0,cursor_column,'right',move)
            show_square(size,square_list)
            cross(cursor_row,cursor_column,move)
            choose(size)
            ylistpos+=1
            tracer(1,0)
            sleep(0.1)
            print(cursor_column,cursor_row)

        elif keyboard.is_pressed('right'):
            cursor_row=cursor_row+move
            clearscreen()
            tracer(0,0)
            arrow(cursor_row,500,'down',move)
            arrow(0,cursor_column,'right',move)
            show_square(size,square_list)
            cross(cursor_row,cursor_column,move)
            choose(size)
            xlistpos+=1
            tracer(1,0)
            sleep(0.1)
            print(cursor_column,cursor_row)

        elif keyboard.is_pressed('left'):
            cursor_row=cursor_row-move
            clearscreen()
            tracer(0,0)
            arrow(cursor_row,500,'down',move)
            arrow(0,cursor_column,'right',move)
            show_square(size,square_list)
            cross(cursor_row,cursor_column,move)
            choose(size)
            xlistpos-=1
            tracer(1,0)
            sleep(0.1)
            print(cursor_column,cursor_row)

        elif keyboard.is_pressed('c'):
            clearscreen()
            tracer(0,0)
            arrow(cursor_row,500,'down',move)
            arrow(0,cursor_column,'right',move)
            square(cursor_row,cursor_column,move,square_list,xlistpos,ylistpos)
            show_square(size,square_list)
            cross(cursor_row,cursor_column,move)
            choose(size)
            tracer(1,0)
            sleep(0.1)
            print(cursor_column,cursor_row)

        
        print(xlistpos,ylistpos)
        sleep(0.01)

        
        

select,size=Picross_selection(Picross_list)
control(size,Player_list,Picross_list[select])   #launch game

        