import string
from tile import Board

class PlayerMoves:
    valid_player = []

    def __init__(self, board, player_pieces, computer_pieces, fromposition, toposition, player):
        self.board = board
        self.player_pieces = player_pieces
        self.computer_pieces = computer_pieces
        self.frompositionx = int(fromposition[0])
        self.frompositiony = int(fromposition[1])
        self.topositionx = int(toposition[0])
        self.topositiony = int(toposition[1])
        self.player = player
        self.check()

    def check(self):
        if self.frompositionx < 0 or self.frompositionx >= len(self.board) or self.frompositiony < 0 or self.frompositiony >= len(self.board[0]):
            print("Invalid move! Coordinates out of bounds.")
            return False

        if self.topositionx < 0 or self.topositionx >= len(self.board) or self.topositiony < 0 or self.topositiony >= len(self.board[0]):
            print("Invalid move! Coordinates out of bounds.")
            return False

        if self.player == "c" and self.board[self.frompositionx][self.frompositiony] in self.computer_pieces:
            self.displayoptions()
            return False

        if self.player == "p" and self.board[self.frompositionx][self.frompositiony] in self.player_pieces:
            self.displayoptions()
            return False

    def displayoptions(self):
        if self.player == "c" and self.board[self.topositionx][self.topositiony] in self.player_pieces:
            print("An opponent's piece is occupying the position.")
            return False

        if self.player == "p" and self.board[self.topositionx][self.topositiony] in self.computer_pieces:
            print("An opponent's piece is occupying the position.")
            return False

        if self.player == "p" and self.board[self.topositionx][self.topositiony] == '---':
            self.valid_player.append(f"{self.topositionx}{self.topositiony}")
            return True
        if self.player == "c" and self.board[self.topositionx][self.topositiony] == '---':
            self.valid_player.append(f"{self.topositionx}{self.topositiony}")
            return True

if __name__ == "__main__":
    board = Board(8, 8)
    board.display()

    while True:
        from_pos = input("Enter position to move from (row,col): ")
        if from_pos.lower() == 'q':
            break
        to_pos = input("Enter position to move to (row,col): ")
        if to_pos.lower() == 'q':
            break
        
        player_move = PlayerMoves(board.board, board.player_pieces, board.computer_pieces, from_pos.split(','), to_pos.split(','), 'p')
        if player_move.check():
            print("Valid move!")
        else:
            print("Invalid move! Try again.")
