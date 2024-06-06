from tabulate import tabulate
import random


board=[
    ["-","a","-","b","-","c","-","d"],
    ["e","-","f","-","g","-","h","-"],
    ["-","i","-","j","-","k","-","l"],
    [0, "-",0, "-",0, "-",0, "-"],
    [ "-",0, "-",0, "-",0, "-",0],
    ["ii", "-","jj", "-","kk", "-","ll", "-"],
    [ "-","ee", "-","ff", "-","gg", "-","hh"],
    ["aa", "-","bb", "-","cc", "-","dd", "-"],
]

print(tabulate(board))
character=input("enter the player you want to move:")
move=input("enter either left of right:")

def isvalidmove(intentline,indexofplayer):
    opponentplayers=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
    userplayers=["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii","jj", "kk", "ll"]

    print(board[intentline])

   #the next line
   # print (f"{board[intentline][indexofplayer-1]} currently occupies this position")

    #the next next line
    #print (f"hello {board[intentline-1][indexofplayer-2]}")

   
    #to check if the move player wants to move is occupied by a collegue player
    if board[intentline][indexofplayer-1] in userplayers:
       
       print(f"player {character} can not move to {move} because {board[intentline][indexofplayer-1]} is there ")
       

    #to check if move is within the board 
    #there is a bug here
    elif board[intentline][indexofplayer-1] == None:
       
       print(f"player {character} can not move to {move} BECAUSE {board[intentline][indexofplayer-1]} is NONE OUTISEDE BOUNDS")
      
    #to check if the move player wants to move is empty 
    elif board[intentline][indexofplayer-1] ==0:
       
       print(f"player {character} can move to {move} because it is empty")

    #to check potential capture move
    elif board[intentline][indexofplayer-1] in opponentplayers and board[intentline-1][indexofplayer-2] == 0:
       
       board[intentline][indexofplayer-1]=0
       board[intentline-1][indexofplayer-2]=character


       print(f"player {character} can capture {board[intentline][indexofplayer-1]} to {move}") 

def findplayerfunction(character,move):
    for i in range(8):
        if character in board[i]:
            indexofplayer=board[i].index(character)
            print(f"the indexx of player {character} is {indexofplayer} in line {i}")
            isvalidmove(i-1,indexofplayer)

findplayerfunction(character, move)