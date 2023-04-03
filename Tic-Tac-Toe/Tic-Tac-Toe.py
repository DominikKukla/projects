from random import randrange

# Creating the game board.
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for x in range(0, 3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   "+str(board[x][0])+"   |   "+str(board[x][1])+"   |   "+str(board[x][2])+"   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            square = int(input("Enter your move: "))
            if square <= 0 or square >= 10:
                print("This number is out of bounds.")
                continue
            elif square != board[(square-1)//3][(square-1) % 3]:
                print("This square is occupied.")
                continue
            else:
                board[(square-1)//3][(square-1) % 3] = 'O'
                break
        except BaseException:
            print("This is not a valid number.")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free = []
    for row in range(0, 3):
        for col in range(0, 3):
            if type(board[row][col]) == int:
                free.append((row, col))
    return free


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    if (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or \
       (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
        return sign
    for x in range(0, 3):
        if (board[x][0] == sign and board[x][1] == sign and board[x][2] == sign) or \
           (board[0][x] == sign and board[1][x] == sign and board[2][x] == sign):
            return sign


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free = make_list_of_free_fields(board)
    if len(free) != 1:
        rng = randrange(len(free)-1)
    else:
        rng = 0
    board[free[rng][0]][free[rng][1]] = 'X'

#
# Game loop; There will be no more than 5 rounds.


for x in range(0, 5):
    # Computer makes a move.
    draw_move(board)

    # Checking if computer won the game or if the game ends in a tie.
    if victory_for(board, 'X') == 'X':
        print("Computer won!")
        break
    elif x == 4:
        print("Tie!")
        break

    # Board is displayed onto the screen.
    display_board(board)

    # Player makes a move.
    enter_move(board)

    # Checking if player won the game.
    if victory_for(board, 'O') == 'O':
        print("You won!")
        break

# Displaying the final state of the board and ending the game.
display_board(board)
print("GG!")
