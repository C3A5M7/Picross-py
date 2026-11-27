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

screen = Screen()
screen.setup(width=1100, height=1100)


Picross_list=[[[[1,0,1,0,1],
                [1,1,1,1,1],
                [0,1,1,1,0],
                [1,1,1,1,1],
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

              [[[0,1,1,1,1],
                [0,0,1,0,1],
                [0,0,1,1,1],
                [0,0,1,0,0],
                [0,1,1,1,0]],'P like picross ;)']]  #List of all curent picross  [LIST[Picross[rows0[Column0,Column1,ect]],Name]]
print(Picross_list[0][0])
Solution_list=[]            #Current playing picross 
Player_list=[]              #Squares placed by player
Numbers_list=[[[[1,1,1],[5],[3],[5],[5]],[[2,2],[4],[5],[4],[2,2]]],
              [[[15],[2,2],[2,9,2],[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,9,2],[2,2],[2,1,2],[2,3,2],[2,1,3,2],[2,2],[2,3],[15]],[[15],[15],[1,1],[1,6,1,1],[1,6,3,1],[1,1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1,1],[1,6,1,1],[1,6,1,1],[1,2],[15],[15]]],
              [[[1,1,4],[1,1,6],[3,2,2],[1,2,2,1],[1,2,1,1],[1,5,1],[1,1,2],[1,5],[1],[7]],[[5],[1,3],[3,1],[3,1],[6,1],[3,1,1,1],[2,1,1,1,1],[2,3,1,1],[3,2,1],[7,1]]],
              [[[1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[7],[2,7],[10],[9],[8],[6]],[[2],[3],[3],[10],[6],[10],[6],[10],[6],[8]]],
              [[[2],[4],[4],[10],[2,7],[2,5],[1,4],[8],[3,3],[3,3]],[[2,1],[3,3],[1,5],[4,2],[8],[8],[8],[7],[3,3],[2,1]]],
              [[[2],[4],[6],[8],[10],[10],[10],[2,2,2],[4],[6]],[[3],[5],[6,1],[6,2],[10],[10],[6,2],[6,1],[5],[3]]],
              [[[0],[7],[3,4],[2,5],[1,6],[15],[1,1],[1,1,2,2],[12],[11],[1,5],[1,6],[2,7],[11],[0]],[[2],[3,1,3],[2,1,2,2],[1,1,2,1],[2,1,3,1],[1,1,2,1],[1,1,2,1],[1,1,2,2],[1,2,3,3],[5,7],[5,6],[4,6],[4,7],[3,2,3],[2]]],
              [[[9],[13],[15],[5,5],[4,1,1,4],[4,1,1,4],[7],[9],[3,3],[3,3,3],[3,3,3],[4,3,4],[5,5],[13],[13]],[[4],[5,4],[5,6],[6,8],[4,9],[3,5,3],[3,2,3,2],[3,2,3,2],[3,2,3,2],[3,5,3],[4,9],[6,8],[5,6],[5,4],[4]]],
              [[[4],[1,1],[3],[1],[3]],[[0],[1,1],[5],[1,1,1],[3]]]]         #[Picross[[Rows1],[Rows2]],[Columns1]]]



print(Numbers_list[0])


def start_player_list(size):
    P_list=[]
    for i in range (size):
        P_list.append([])
        for i in range (size):
            P_list[-1].append(0)
    return P_list


hideturtle()


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
    if size == 100:   #give the number of px to move to be aligned with the grid 
        mult=5
    if size == 50:
        mult=10
    if size == 33:
        mult=15
    if size == 25:
        mult=20
    if size == 20:
        mult=25
    setheading(90)
    color('grey')
    for a in range (columns+1):
        if a+1 == 6 or a+1 == 11 or a+1 == 16 or a+1 == 21 or a+1 == 26 :
            if a+1 != mult+1:
                pensize(2)
                color('coral2')
        penup()
        goto(a*size,0)
        pendown()
        forward(size*(rows))
        pendown()
        color('grey')
        pensize(1)

    setheading(0)
    for b in range (rows+1):
        if b+1 == 6 or b+1 == 11 or b+1 == 16 or b+1 == 21 or b+1 == 26 :
            if b+1 != mult+1:
                print(b+1,mult+1)
                color('coral2')
                pensize(2)
        penup()
        goto(0,b*size)
        pendown()
        forward(size*(columns))
        color('grey')
        pensize(1)
    color('black')

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
    pensize(3)
    color ('grey')
    penup()
    goto(x,y)
    setheading(90)
    forward ((size/2)*0.8)
    setheading(-45)
    pendown()
    for i in range (4):
        forward (sqrt((size/2*0.8)**2+(size/2*0.8)**2))
        right(90)
    penup()
    color('black')
    pensize(1)

def X_mark(x,y,size,X_list,xlist,ylist,square_list):
    """ penup()
    setheading(-45)
    goto(x-size/8,y-size/8)
    pendown()
    forward((6*size)/8)
    penup()
    setheading(45)
    goto(x-size/8,y-(7*size)/8)
    pendown()
    forward((6*size)/8)
    penup()
    setheading(0) """
    if square_list[ylist][xlist]==1 or X_list[ylist][xlist]==1 :
        square_list[ylist][xlist]=0
        X_list[ylist][xlist]=0


    elif square_list[ylist][xlist]==0:
        X_list[ylist][xlist]=1




def show_X (size,X_list):   #draws squares on picross with the player_list

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

    pensize(3)
    penup()
    setheading(0)
    for y in range (len(X_list[-1])):
        for x in range (len(X_list[-1])):
            if X_list[y][x]==1:
                color('chocolate')
                
                goto(x*mult,-y*mult+((size-1)*mult))
                setheading(45)
                pendown()
                forward(sqrt(mult**2+mult**2))
                penup()
                setheading(0)
                forward(-mult)
                setheading(-45)
                pendown()
                forward(sqrt(mult**2+mult**2))
                penup()
                setheading(0)
    setheading(0)
    pensize(1)
    color('black')

   

def square (x,y,size,square_list,xlist,ylist,X_list):   #draw a square at coordinate to place a square on the picross 
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
    if square_list[ylist][xlist]==1 or X_list[ylist][xlist]==1 :
        square_list[ylist][xlist]=0
        X_list[ylist][xlist]=0


    elif X_list[ylist][xlist]==0:
        square_list[ylist][xlist]=1



    
        
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
            if square_list[y][x]==1:
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

        



    
def Numbers(size,selected,List_num):
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

    Current_picross=List_num[selected]  # current list --->. [ [[N,N] , [N] , [N,N,N,N] ]   ,   [[N,N] , [N] , [N,N,N,N] ]      ]

    # starting position for horizontal text y=-30 and add -20 per supplementary lines and x is at first move/2 and + move * actual columns

    # starting position for Vertical text x=-30 and add -20 per supplementary lines and y is at first move/2 and + move * actual rows

    


    


    for a in range (len(Current_picross[0])):
        for b in range (len(Current_picross[0][a])):
            penup()
            goto((-30+(-20*len(Current_picross[0][a])))+b*20,488-(move/2+(move*a)))
            pendown()
            write(Current_picross[0][a][b], align="center", font=("Courier", 22, "normal"))


    for a in range (len(Current_picross[1])):
         for b in range (len(Current_picross[1][a])):
            penup()
            goto((move/2+(move*a))+0,(-30+(-20*len(Current_picross[1][a])))+b*20)
            pendown()
            write(Current_picross[1][a][(len(Current_picross[1][a])-1)-b], align="center", font=("Courier", 22, "normal"))
                    
        




    

    


def control (size,square_list,Solve_list,select,Num_list,X_list):

    if size == 5:   #give the number of px to move to be aligned with the grid and is also used in the arrow size
        move=100
        frame_limit=20
    if size == 10:
        move=50
        frame_limit=10
    if size == 15:
        move=33
        frame_limit=5
    if size == 20:
        move=25
        frame_limit=3
    if size == 25:
        move=20
        frame_limit=2

    cursor_row=move/2           #set the starting position of the arrows
    cursor_column=move/2+(move*size)-move

    xlistpos=0      #position in the player list
    ylistpos=0

    Victory=0

    Frame_counter=0         #something to count the number of drawed frame since last clear (this help to be less flashing)
    #timestart=round(time(),0)
    #elaspsed=0
          

    tracer(0,0)         #show the screen
    choose(size)
    Numbers(size,select,Num_list)
    #arrow(cursor_row,500,'down',move)
    #arrow(0,cursor_column,'right',move)
    cross(cursor_row,cursor_column,move)
    tracer(1,0)

    while Victory==0:
        if keyboard.is_pressed('up'):
            if (cursor_column/move)+0.5 == size :
                cursor_column=move/2
                #clearscreen()
                tracer(0,0)
                #arrow(cursor_row,500,'down',move)
                #arrow(0,cursor_column,'right',move)
                show_square(size,square_list)
                show_X(size,X_list)
                cross(cursor_row,cursor_column,move)
                choose(size)
                #Numbers(size,select,Num_list)
                ylistpos=size-1
                Frame_counter+=1
                tracer(1,0)
                sleep(0.1)


            else:
                cursor_column=cursor_column+move
                #clearscreen()
                tracer(0,0)
                #arrow(cursor_row,500,'down',move)
                #arrow(0,cursor_column,'right',move)
                show_square(size,square_list)
                show_X(size,X_list)
                cross(cursor_row,cursor_column,move)
                choose(size)
                #Numbers(size,select,Num_list)
                ylistpos-=1
                Frame_counter+=1
                tracer(1,0)
                sleep(0.1)

            

        elif keyboard.is_pressed('down'):
            if (cursor_column/move)+0.5 == 1 :
                cursor_column=move/2+(move*size)-move
                #clearscreen()
                tracer(0,0)
                #arrow(cursor_row,500,'down',move)
                #arrow(0,cursor_column,'right',move)
                show_square(size,square_list)
                show_X(size,X_list)
                cross(cursor_row,cursor_column,move)
                choose(size)
                #Numbers(size,select,Num_list)
                ylistpos=0
                Frame_counter+=1
                tracer(1,0)
                sleep(0.1)

            else:

                cursor_column=cursor_column-move
                #clearscreen()
                tracer(0,0)
                #arrow(cursor_row,500,'down',move)
                #arrow(0,cursor_column,'right',move)
                show_square(size,square_list)
                show_X(size,X_list)
                cross(cursor_row,cursor_column,move)
                choose(size)
                #Numbers(size,select,Num_list)
                ylistpos+=1
                Frame_counter+=1
                tracer(1,0)
                sleep(0.1)

        elif keyboard.is_pressed('right'):
            if (cursor_row/move)+0.5 == size :
                cursor_row=move/2
                #clearscreen()
                tracer(0,0)
                #arrow(cursor_row,500,'down',move)
                #arrow(0,cursor_column,'right',move)
                show_square(size,square_list)
                show_X(size,X_list)
                cross(cursor_row,cursor_column,move)
                choose(size)
                #Numbers(size,select,Num_list)
                xlistpos=0
                Frame_counter+=1
                tracer(1,0)
                sleep(0.1)


            else:
                cursor_row=cursor_row+move
                #clearscreen()
                tracer(0,0)
                #arrow(cursor_row,500,'down',move)
                #arrow(0,cursor_column,'right',move)
                show_square(size,square_list)
                show_X(size,X_list)
                cross(cursor_row,cursor_column,move)
                choose(size)
                #Numbers(size,select,Num_list)
                xlistpos+=1
                Frame_counter+=1
                tracer(1,0)
                sleep(0.1)

        elif keyboard.is_pressed('left'):
            if (cursor_row/move)+0.5 == 1 :

                cursor_row=move/2+(move*size)-move
                #clearscreen()
                tracer(0,0)
                #arrow(cursor_row,500,'down',move)
                #arrow(0,cursor_column,'right',move)
                show_square(size,square_list)
                show_X(size,X_list)
                cross(cursor_row,cursor_column,move)
                choose(size)
                #Numbers(size,select,Num_list)
                xlistpos=size-1
                Frame_counter+=1
                tracer(1,0)
                sleep(0.1)

            else:

                cursor_row=cursor_row-move
                #clearscreen()
                tracer(0,0)
                #arrow(cursor_row,500,'down',move)
                #arrow(0,cursor_column,'right',move)
                show_square(size,square_list)
                show_X(size,X_list)
                cross(cursor_row,cursor_column,move)
                choose(size)
                #Numbers(size,select,Num_list)
                xlistpos-=1
                Frame_counter+=1
                tracer(1,0)
                sleep(0.1)


        elif keyboard.is_pressed('c'):
            #clearscreen()
            tracer(0,0)
            #arrow(cursor_row,500,'down',move)
            #arrow(0,cursor_column,'right',move)
            square(cursor_row,cursor_column,move,square_list,xlistpos,ylistpos,X_list)
            show_square(size,square_list)
            show_X(size,X_list)
            cross(cursor_row,cursor_column,move)
            choose(size)
            #Numbers(size,select,Num_list)
            Frame_counter+=1

            if square_list == Solve_list[0]:
                Victory=1
            tracer(1,0)
            sleep(0.1)

        elif keyboard.is_pressed('x'):
            #clearscreen()
            tracer(0,0)
            #arrow(cursor_row,500,'down',move)
            #arrow(0,cursor_column,'right',move)
            X_mark(cursor_row,cursor_column,move,X_list,xlistpos,ylistpos,square_list)
            print(X_list)
            show_square(size,square_list)
            show_X(size,X_list)
            cross(cursor_row,cursor_column,move)
            choose(size)
            #Numbers(size,select,Num_list)
            Frame_counter+=1

            if square_list == Solve_list[0]:
                Victory=1
            tracer(1,0)
            sleep(0.1)

        """ if timestart<=round(time()-1,0):
            tracer(0,0)
            print(elaspsed)
            elaspsed+=1
            penup()
            goto(-300,200)
            pendown()
            begin_fill()
            color('white')
            goto(-100,200)
            goto(-100,0)
            goto(-300,0)
            goto(-300,200)
            end_fill()
            if elaspsed%10==1:
                Frame_counter==100  #for make the screen clear
            color('black')
            tracer(1,0)
            penup()
            goto(-250,150)
            write('Time : ', align="center", font=("Courier", 16, "normal"))
            goto(-200,150)
            write(round(elaspsed/60,0), align="center", font=("Courier", 16, "normal"))
            goto(-150,150)
            write(elaspsed%60, align="center", font=("Courier", 16, "normal"))
            timestart=round(time(),0)
            color('black')
            tracer(1,0) """


        if Frame_counter > frame_limit :
            clearscreen()
            tracer(0,0)
            show_square(size,square_list)
            show_X(size,X_list)
            cross(cursor_row,cursor_column,move)
            choose(size)
            Numbers(size,select,Num_list)
            Frame_counter=0
            tracer(1,0)


        sleep(0.01)

    tracer(0,0)
    setheading(45)
    for i in range(2000):
        penup()
        goto(1000-i*4,-1000)
        pendown()
        forward(3000)
    
    setheading(0)
    penup()
    goto(-400,400)
    color('white')
    begin_fill()
    pendown()
    for i in range(4):
        forward(800)
        right(90)
    end_fill()
    penup()
    color('black')
    goto(0,100)
    pendown()
    write('You win', align="center", font=("Courier", 48, "normal"))
    penup()
    goto(0,-50)
    pendown()
    write('Picross name :', align="center", font=("Courier", 28, "normal"))
    penup()
    goto(0,-100)
    pendown()
    write(Solve_list[1], align="center", font=("Courier", 22, "normal"))
    penup()
    goto(0,-400)
    pendown()
    write('Press c to exit', align="center", font=("Courier", 16, "normal"))
    hideturtle()
    tracer(1,0)


    exit=0

    while exit==0:
        if keyboard.is_pressed('c'):
            exit=1



size=5        

select,size=Picross_selection(Picross_list)

def start_player_list(size):
    P_list=[]
    for i in range (size):
        P_list.append([])
        for i in range (size):
            P_list[-1].append(0)
    return P_list


Player_list=start_player_list(size)
X_Player_list=start_player_list(size)
control(size,Player_list,Picross_list[select],select,Numbers_list,X_Player_list)   #launch game

        