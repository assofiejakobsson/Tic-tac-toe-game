import random

# Global variabel

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


player = "x"
gameRunning = True
winner = None

# Welcome



# Make a choise


def playerChoise(board):
    print("Welcome to Tic, tac, toe game!")
    print("Game rules: ")
    print("1. The game is played on a grid that's 3 squares by 3 squares.")
    print("2. You are X, the computer is o.")
    print("3. Players take turns putting their marks in empty squares.")
    print("4. The first player to get 3 in a row, is the winner.")
    print("5. You can get three in a row (up, down, across, or diagonally)")

    inp = str(input("Enter p for play or r for restart: "))
    if inp == "r":
        print("")
    elif inp == "p":
        inp = int(input("Enter a number between 1-9: "))
    elif inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = player
    elif inp <= 0 or inp > 9:
        print("The number are incorect! Pleas try another number between 1-9")
    else:
        print("The spot is alredy taken! Pleas try another number between 1-9")


playerChoise(board)


# Game rules

# Exit the game

# Start the game

# Pleas Enter your name

def displayBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


displayBoard(board)


# Check If there is tree in a row horizontally

def checkHorizont(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

# Check If there is tree in a row vertically


def checkVertic(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

# Check If there is tree in a row diagonally


def checkDiagon(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

# Check tie


def checkTie(board):
    global gameRunning
    if "-" not in board:
        displayBoard(board)
        print("It,s a tie!")
        gameRunning = False


# Check winner


def checkWinner():
    if checkHorizont(board) or checkVertic(board) or checkDiagon(board):
        print(f"Winner is {winner}")


# Switch player


def switchPlayer():
    global player
    if player == "x":
        player = "o"
    else:
        player = "x"


# computer choise


def computer(board):
    while player == "o":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "o"
            switchPlayer()


# Check for wrong input and print error message


# Message Win, lose or a tie

# Game lop


while gameRunning:
    displayBoard(board)
    playerChoise(board)
    checkTie(board)
    checkWinner()
    switchPlayer()
    computer(board)
    checkTie(board)
    checkWinner()

