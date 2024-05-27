					**Checkers** 

is a classic two-player board game that has been enjoyed by people of all ages for generations. It is a strategy game that requires players to move their pieces across the board, capturing their opponent's pieces and ultimately trying to reach the other end of the board with one of their pieces to become a king.

The  goal is to provide an overview of the game, breaking it down into several classes that work together to provide the game's functionality. We will cover the installation and setup process, the main class, the game class, the board class, the tile class, the piece class, the pawn class, and the king class.

What we need 
board An 8x8 two-dimensional list, initialized to the above starting position for a checkers board. The board will contain integer values, corresponding to the various things that can occupy spaces on the board. 
            ▪  empty space 
            ▪ white checker 
            ▪ red checker 
            ▪ white king 
            ▪ red king 
              

    • whoseToMove 
        ◦ keeps track of whose turn it is to move. Initializes to "white" 
    • isWon 
        ◦ keeps track of whether the game has been won or not. If the game has been won, this field will either "red" or "white", depending on who has won. 
Follow the following methods














    • parseMove() 
        ◦ The user will input moves to a command line interface in the following form: 
            ▪ "YX YX ..." 
        ◦ Y and X are numbers between 0 and 7, which correspond to co-ordinates on the game board. 
        ◦ The first coordinate entered is the coordinate of the piece you wish to move. 
        ◦ The second is where you wish to move it to. 
        ◦ This function must return a list of tuples. 
            ▪ Each tuple must be of length two. 
            ▪ The first element is the row (Y) 
            ▪ The second element is the column (X) 
        ◦ This string may have many coordinates (for when jumping multiple pieces). 
        ◦ If for any reason the string provided is not a valid set of coordinates (out of range, no spaces, etc.), raise a ValueError. 
        ◦ There are some test cases below. 
    • checkWinner() 
        ◦ Red wins if there are no white pieces remaining. 
        ◦ White wins if there are no red pieces remaining. 
        ◦ This method updates the isWon attribute accordingly. 
        ◦ 
    • 
    • 
    • changeTurn()
        ◦ If it's currently Red's turn, change to White, and vice versa. 
        ◦ If you decided to keep any extra data relating to the following, it should be updated: 
            ▪ Which board values are currently active 
            ▪ Which board values are currently enemies 
            ▪ Which direction pieces are travelling on the board 
            ▪ Any other movement related data that you may wish to keep. 
    • move()
        ◦ Given a move, expressed as a string, modify the class attributes to reflect the move encoded in the string. 









        ◦ You may assume that the input represents a valid move. 
        ◦ The move operation will consist of three things, two of which we have already written methods for: 
            ▪ Updating the board 
            ▪ Changing whose turn it is 
            ▪ Checking to see if the game is won, and updating appropriately. 
    • checkValidMove()
        ◦ In this algorithm, we are going to separate the code that checks that a move is valid from the code that actually mutates the state of the board. 
        ◦ Given a move, expressed as a string, return True if this move is a valid move for the player whose turn it is. 
        ◦ Bear in mind that the input is an unparsed string, so you may want to use one of the other methods in your class to parse it (waggles eyebrows). 
        ◦ No move is valid on a game that has been won. 
        ◦ 


**Rules**
Winning the game:
You win the game if you lose all your Mules. You lose the game if you are
forced to promot. You also lose the game if you lose all your
regular pieces.
• By capturing all of your OPPONENT's regular pieces
• By losing all YOUR pieces
• By forcing your OPPONENT to promote a Mule (that is, move it to the
last row)
Or, put another way, you lose the game in one of 3 ways:
• By losing all of YOUR regular pieces
• By capturing all of your OPPONENT's  pieces
• By promoting YOUR Mule (it ends up on the row furthest away from
you)

You Must Jump if Possible
If a jump is available for one of your pieces, you must make that jump. If
more jumps are available with that same piece, you must continue to jump
with it until it can jump no more. To make the second and third jump with a
piece, you do not need to click that piece again. Just click the next space to
which it will jump.
If more than one of your pieces has a jump available at the start of your
turn, you can choose which piece you will move. But then you must make all
the jumps available for that piece.
**Crowning**
When one of your checkers reaches the opposite side of the board, it is
crowned and becomes a King. Your turn ends there.
A King can move backward as well as forward along the diagonals. It can
only move a distance of one space.
A King can also jump backward and forward. It must jump when possible,
**Jumping**
If one of your opponent’s checkers is on a forward diagonal next to one of
your checkers, and the next space beyond the opponent’s checker is empty,
then your checker must jump the opponent’s checker and land in the space
beyond. Your opponent’s checker is captured and removed from the board
and it must take all jumps that are available to it. In each jump, the King can
only jump over one opposing piece at a time, and it must land in the space
just beyond the captured piece. The King can not move multiple spaces
before or after jumping a pi
