# Picross python



Picross From Mario's Picross On Game Boy and various picross S games from nintendo switch


>[!NOTE]
>For MacOs must be run as admin with Sudo and accessibility 





> [!NOTE] 
>  Ported Picross are the only thing made with help of Ai in this code because porting 7 (2 to 8) picross by hand from 5x5 to 15x15
would take so much time and be boring .

>[!NOTE]
>   Some Picross like 2,7,8 are large (15x15) and can be quite 
> slow for more representative and playable Picross try the 10x10 and 5x5 ones

## Base of game

### - Controls
This is a Picross game so you need to know the basics of Picross:

You can :
- Move 
- Place Block (1) and Diamonds(2)

(1) - The Block is what you need to place on precise coordinate to make the shape of the Picross and finish the Picross

(2) - Technically, the diamond is optional but basically the diamond can helps you figuring out where to place the remainings blocks

### Goal of the game

In Picross, you have a shape (generally a square) of X*X blocks with numbers on the sides.

Each numbers is how many block you have in the line for example :

2 3 1 

This mean in first you 2 consecutives blocks and a void(diamond) of 1 or more after you get 3 consecutives blocks and a void or more and finally one block.

### Tips

if your grid is for example 10 by 10 and you need just to place 6 blocks , what you can do is count the number of block from each side, and then place block at the overlapping coordinate

6 | # # # # # # _ _ _ _ | from left to right 

6 | _ _ _ _ # # # # # # | from right to left

6 | + + + + X X + + + + | only the two at center are overlapping

X= blocks (overlapping ones)  
+= non-overlapping blocks   
#= counting block from each side.  
_= No blocks


Take your time you are not limited by time


## Features
- Teleport cursor when on the side to get to the other side
- Blocks and Diamonds
- Various Picross from 5x5 to 15x15
- Main menu

## Included Picross
<ol>
<li>Castle from Picross S (5X5)</li>
<li>Game Boy from Mario's Picross (15X15)</li>
<li>Snail from Mario's Picross (10x10)</li>
<li>Glove from Mario's Picross (10x10)</li>
<li>Star from Mario's Picross (10x10)</li>
<li>Spike from Mario's Picross (10x10)</li>
<li>Burger from Mario's Picross (15X15)</li>
<li>Phone from Mario's Picross (15X15)</li>
<li>P like Picross made by myself (5X5)</li>
</ol>



## AI use
- As mention above AI was used to help me port picross into list because it would take a lot of time (i still made the plan of list but the value are from the AI and tested after to see if everything was correct)

- No other part of the code was made by or assisted by AI

- only 2,3,4,5,6,7,8 are ported by AI 1 and 9 are by me

