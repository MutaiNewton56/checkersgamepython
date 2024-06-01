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

print(f"player {character} moves to {move}")


for i in range(8):
        if character in board[i]:
            indexofplayer=board[i].index(character)


def isvalidmove(board,character,move):

   
   pass  

def findplayerfunction(character,move):
    if move=="left":
      for i in range(8):
        if character in board[i]:
            indexofplayer=board[i].index(character)
            print(indexofplayer,i)

findplayerfunction(character, move)