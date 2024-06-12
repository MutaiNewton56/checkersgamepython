class Checkers:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.initialize_board()

    def initialize_board(self):
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = 'c'

        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = 'p'

    def print_board(self):
        print(" ", end=" ")
        for col in range(8):
            print(f" {col} ", end=" ")
        print()
        print(" +---+---+---+---+---+---+---+---+")
        for row in range(8):
            print(row, end="|")
            for col in range(8):
                print(f" {self.board[row][col]} |", end="")
            print()
            print(" +---+---+---+---+---+---+---+---+")
    
    def move_piece(self, start_row, start_col, end_row, end_col, player):
        piece = self.board[start_row][start_col]
        captured_piece_pos = None  # Initialize captured piece position
        if piece != player:
            print(f"Invalid move. You can only move '{player}' pieces.")
            return False, captured_piece_pos
        if piece == ' ':
            print("No piece at starting position.")
            return False, captured_piece_pos
        if player == 'p' and end_row > start_row:  # Player 'p' moves upwards
            print("Invalid move. Only move upwards.")
            return False, captured_piece_pos
        if player == 'c' and end_row < start_row:  # Computer 'c' moves downwards
            print("Invalid move. Only move downwards.")
            return False, captured_piece_pos
        if abs(start_row - end_row) != abs(start_col - end_col):
            print("Invalid move. Moves must be diagonal.")
            return False, captured_piece_pos
        if abs(start_row - end_row) > 2:
            print("Invalid move. Can only move one or two spaces.")
            return False, captured_piece_pos
        if abs(start_row - end_row) == 2:
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            if self.board[mid_row][mid_col] == ' ':
                print("Invalid move. Must jump over opponent's piece.")
                return False, captured_piece_pos
            captured_piece_pos = (mid_row, mid_col)  # Set captured piece position
            self.board[mid_row][mid_col] = ' '
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = ' '
        print("Valid move!")
        return True, captured_piece_pos  # Return captured piece position
    
def main():
    game = Checkers()
    print("Welcome to Checkers!")
    print("To move a piece, enter the starting position and then the ending position.")
    print("For example: '2 1 3 2' moves a piece from row 2, col 1 to row 3, col 2.")
    input("Press Enter to start the game...")
    while True:
        game.print_board()
        start_input = input("Enter start position (row col): ").split()
        end_input = input("Enter end position (row col): ").split()
        if len(start_input) != 2 or len(end_input) != 2:
            print("Invalid input. Please enter row and column separated by space.")
            continue
        try:
            start_row, start_col = map(int, start_input)
            end_row, end_col = map(int, end_input)
        except ValueError:
            print("Invalid input. Please enter integers.")
            continue
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            print("Invalid input. Position out of range.")
            continue
        valid_move, captured_piece_pos = game.move_piece(start_row, start_col, end_row, end_col, 'p')
        if not valid_move:
            print("Invalid move. Please try again.")
            continue
        if captured_piece_pos:
            print(f"Piece captured at position {captured_piece_pos} and removed.")    

if __name__ == "__main__":
   main()