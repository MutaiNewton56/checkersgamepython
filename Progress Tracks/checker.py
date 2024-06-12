from tabulate import tabulate

import random

board=[
    ["-","a","-","b","-","c","-","d"],
    ["e","-","f","-","g","-","h","-"],
    ["-","i","-","j","-",0,"-","l"],
    [0, "-",0, "-",0, "-",0, "-"],
    [ "-",0, "-",0, "-","k", "-",0],
    ["ii", "-","jj", "-","kk", "-","ll", "-"],
    [ "-","ee", "-","ff", "-","gg", "-","hh"],
    ["aa", "-","bb", "-","cc", "-","dd", "-"],
]



def isvalidmove(character,move):
    
    opponentplayers=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
    userplayers=["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii","jj", "kk", "ll"]

    intentline=0
    currentline=0
    indexofplayer=0
    intentposition=0
    
   

    for i in range(8):
      if character in board[i]: 
            currentline=i
            intentline=i-1
            indexofplayer=board[i].index(character)
            if move=="left":
               intentposition=(indexofplayer-1)

              
            if move =="right":
               intentposition=indexofplayer+1
               

      #  print(board[intentline])
      #  print(f"current line is {currentline}")
      #  print(f"index inside isvalid {indexofplayer}")
      #  print(f"intentline inside isvalid {intentline}")
      #  print(f"intentposition inside isvalid {intentposition}")
      #  print (f"inside isvalid the index {indexofplayer}of player{character} is line{intentline}")


    
    #to check if move is within the board 
    
    if not (0 <= intentline <= 7) or not (0 <= intentposition <= 7):
       
       print(f"player {character} can not move {move} BECAUSE is OUTISEDE BOUNDS")


       #if this condition is satisfied.. ie the player move is within the board we check the other rules
    else:
      
         

         
         #to check if the move player wants to move is occupied by a collegue player
         if board[intentline][intentposition] in userplayers:
            
            print(f"player {character} can not move to {move} because {board[intentline][intentposition]} is there ")
            

         #to check if the move player wants to move is empty 
         elif board[intentline][intentposition] ==0 and not (0 <= intentline <= 7) or not (0 <= intentposition <= 7):
            
            print(f"player {character} can move to {move} because it is empty")

         #to check potential capture move
         elif board[intentline][intentposition] in opponentplayers and board[intentline-1][intentposition-1] == 0:

            print(f"player {character} has captured {board[intentline][intentposition]} to {move}") 
         
            #to remove and replace the captured player and move the player forward two times
            board[intentline][intentposition]=0
            board[intentline-1][intentposition-1]=character
            board[currentline][indexofplayer]=0







def findplayerfunction(character):
    
    for i in range(8):
      if character in board[i]: 
         
            indexofplayerr=board[i].index(character)
            print(f"the indexx of player {character} is {indexofplayerr} in line {i}")
            #isvalidmove(i-1,indexofplayer)
            return True
            
      
    print(f"player {character} is not in the board")
    return False
         
        




def main():
   isplaying=True
   while isplaying:
      print("*************")
      print("*************")
      print(tabulate(board))
      print("*************")
      print("*************")

      print ("1: play.")
      print ("2: exit.")

      choice=input("enter your choice: ")

      if choice == "1":
         character=input("enter the player you want to move: ")

         while not findplayerfunction(character):
            print("Invalid character. Please try again")
            character=input("enter the player you want to move: ")
         
         move=input("enter either left of right: ")
          

         isvalidmove(character,move)
         print(character)


         
            
            

          
      
      elif choice == "2":
         isplaying=False

      else:
         print("invalid choice")


      

         
         
        


if __name__ == "__main__":
    main()