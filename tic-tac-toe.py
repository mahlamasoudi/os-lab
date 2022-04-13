import time
import random
import colorama
from colorama import Fore
colorama.init()
#---------------------------------------------------------------------
def show_game_board():
    for row in game:
        for item in row:
            if item=="-":
                print(item,end=" ")
            if item=="X":
                print(Fore.YELLOW + item + Fore.RESET,end=" ")
            if item=="O":
                print(Fore.BLUE + item + Fore.RESET,end=" ")   
        print()
#-----------------------------------------------------------------------
def check(playerNumber,char):
    if game[0][0]==game[0][1]==game[0][2]==char:
        print("player",playerNumber,"win")
        return 1
    if game[1][0]==game[1][1]==game[1][2]==char:
        print("player",playerNumber,"win")
        return 1
    if game[2][0]==game[2][1]==game[2][2]==char: 
        print("player",playerNumber,"win")
        return 1 

    if game[0][0]==game[1][0]==game[2][0]==char:
        print("player",playerNumber,"win")
        return 1  
    if game[0][1]==game[1][1]==game[2][1]==char:
        print("player",playerNumber,"win")
        return 1
    if game[0][2]==game[1][2]==game[2][2]==char:
        print("player",playerNumber,"win")
        return 1

    if game[0][0]==game[1][1]==game[2][2]==char:
        print("player",playerNumber,"win")
        return 1
    if game[2][0]==game[1][1]==game[0][2]==char:
        print("player",playerNumber,"win")
        return 1
    return 0
#---------------------------------------------------------------------------       
tedadbazi=0
game=[['-' ,'-' ,'-' ],
     ['-' ,'-' ,'-' ],
     ['-' ,'-' ,'-' ]]
options=[0,1,2]
print("1-play with computer 2-play with other    select")
select=int(input())
for row in game:
    for item in row:
        print(item,end=" ")
    print()
start = time.time()

#player1 vs player2
if select==2:
    while True:
    #player1
        while(True):
            print("player1 turn")
            row=int(input("row:"))
            col=int(input("col:"))
            if game[row][col]=="-":
                game[row][col]="X"
                tedadbazi=tedadbazi+1
                break
            else:
                print("be careful")
        show_game_board()       
        if check(1,"X")==1:
            break 
        if tedadbazi==9:
            print("no winner")
            break 
    #player2
        while(True):
            print("player2 turn")
            row=int(input("row:"))
            col=int(input("col:"))
            if game[row][col]=="-":
                game[row][col]="O"
                tedadbazi=tedadbazi+1
                break
            else:
                print("be careful")
        show_game_board()
        if check(2,"O")==1:
            break

#player vs computer        
elif select==1:
    while True:
    #player
        while(True):
            print("player turn")
            row=int(input("row:"))
            col=int(input("col:"))
            if game[row][col]=="-":
                game[row][col]="X"
                tedadbazi=tedadbazi+1
                break
            else:
                print("be careful")
        show_game_board()       
        if check(1,"X")==1:
            break 
        if tedadbazi==9:
            print("no winner")
            break 
    #computer
        print("computer turn")
        while(True):
            row=random.choice(options)
            col=random.choice(options)
            if game[row][col]=="-":
                game[row][col]="O"
                tedadbazi=tedadbazi+1
                break
        show_game_board()
        if check("computer","O")==1:
            break    
print("Play Time: " + str( time.time() - start ))           