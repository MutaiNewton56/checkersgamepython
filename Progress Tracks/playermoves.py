#this code calls a function that checks if the player the user selects is valid
#and if the the move he wants to make is also valid.
#not outside the board
#not when occupied
#not when occupied
from tile import board

class playermoves():
    valid_player=[]

    def __init__(self,board,player_pieces,computer_pieces,fromposition,toposition,player):
        self.board=board
        self.player_pieces=player_pieces
        self.computer_pieces=computer_pieces
        self.frompositionx=int(fromposition[0])
        self.frompositiony=int(fromposition[1])
        self.topositionx=int(toposition[0])
        self.topositiony=int(toposition[1])
        self.player=player
        self.check()

    
    def check(self):
        #im to receive input in the form of 
        # p20... meaning the player. the x axis and y axis
        
        #to check if the one playing has such a piece comp
        if self.player=="c" and self.board[self.frompositionx][self.frompositiony] in self.computer_pieces:
            self.displayoptions()
            return False
        
        #to check if the one playing has such a piece user
        if self.player=="p" and self.board[self.frompositionx][self.frompositiony] in self.player_pieces:
            self.displayoptions()
            return False

    
    def displayoptions(self):

        #to check if the intended position is occupied by another player==computer
        if self.player=="c" and self.board[self.topositionx][self.topositiony] in self.player_pieces:
            #check_potential_capture()
            print("an opponents piece is occupying the position")
            return False
        
        #to check if the intended position is occupied by another player==user
        if self.player=="p" and self.board[self.topositionx][self.topositiony] in self.computer_pieces:
            #check_potential_capture()
            print("an opponents piece is occupying the position")
            return False
        
        #to check if the intended position is empty
        if self.player=="p" and self.board[self.topositionx][self.topositiony] == '---':
            #to add the new player to the pieces
            #self.player_pieces.append(f"p{self.topositionx}{self.topositiony}")
            self.valid_player.append(f"{self.topositionx}{self.topositiony}")
            #to add the new player to the board
            return True
        if self.player=="c" and self.board[self.topositionx][self.topositiony] == '---':
            #to add the new player to the pieces
            #self.computer_pieces.append(f"c{self.topositionx}{self.topositiony}")
            self.valid_player.append(f"{self.topositionx}{self.topositiony}")
            #to add the new player to the board
            return True
        
        ###within the board
        
#compmoves randomly ninani anataka acheze



   
    