board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

player = "x"
computer = "o"

# Welcome

# Make a choise


def playerChoise(board):
    inp = int(input("Enter a number between 0-9: "))
    if inp >= 0 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = player
    else:
        print("The spot is alredy taken!")


print(playerChoise(board))


# Game rules

# Exit the game

# Start the game


def displayBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


print(displayBoard(board))

# Pleas Enter your name

# Check If there is tree in a row horizontally

# Check If there is tree in a row vertically

# Check If there is tree in a row diagonally

# Check for wrong input and print error message

# Message Win, lose or a tie
