# Imports

import random  # Used for the computer's selection.
import os  # Used to clear the screen.
import time  # Used to set time before another method is executed.

# Global variabel

refBoard = ["1", "2", "3",
            "4", "5", "6",
            "7", "8", "9"]

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

player = "x"
gameRunning = True
winner = None
input_correct = False


def restartGame():
    """
    Used when a player wants to play again. Gives the user the options to
    play again, play rules, or exit the game. With a suitable message.
    """
    inp = str(input("Enter p for play or r for ruels or e for exit: \n"))
    os.system('clear')
    if inp == "e":
        print("Thank you for playing")
        inp = str(input("If yo want to play agin enter p: \n"))
        os.system('clear')
    elif inp == "r":
        gameRules()
        os.system('clear')
    elif inp == "p":
        os.system('clear')
    else:
        print("Wrong input")
        restartGame()
        os.system('clear')


def gameRules():
    """
    Shows the game rules. And gives the user the
    option to choose to quit the game or play.
    """
    print("Game rules: ")
    print("1. The game is played on a grid that's 3 squares by 3 squares.")
    print("2. You are x, the computer is o.")
    print("3. Players take turns putting their marks in empty squares.")
    print("4. The first player to get 3 in a row, is the winner.")
    print("5. You can get three in a row (up, down, across, or diagonally)")
    inp = str(input("Enter p for play or e for exit: "))
    if inp == "e":
        print("Thank you for playing")
        os.system('clear')
        inp = str(input("If yo want to play agin enter p: \n"))
        os.system('clear')
    elif inp == "p":
        os.system('clear')
    else:
        print("Wrong input")
        restartGame()
        os.system('clear')


def start():
    """
    Displays a welcome text. And gives the user the choice to
    play, read game rules or exit the game. With a suitable message.
    """
    print("Welcome to Tic, tac, toe game!")
    inp = str(input("Enter p for play, r for rules or e for exit: \n"))
    os.system('clear')
    if inp == "e":
        print("Thank you for playing")
        inp = str(input("If yo want to play agin enter p: \n"))
        os.system('clear')
    elif inp == "r":
        gameRules()
        os.system('clear')
    elif inp == "p":
        os.system('clear')
    else:
        print("Wrong input")
        restartGame()
        os.system('clear')


start()


def refereceBoard(refBoard):
    """
    The reference board is displayed when the game
    is running to facilitate UX.
    """
    print("Reference board")
    print("1-" "|"  "-2-" "|" "-3")
    print("4-" "|"  "-5-" "|" "-6")
    print("7-" "|"  "-8-" "|" "-9")


def displayBoard(board):
    """
    The game board is displayed when the game
    is running. And it updates as the user
    and the computer make their choices.
    """
    print("Game board")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def playerChoise(board):
    """
    Makes the user's choice work. And checks that the input
    is within the limits of the game.
    And displays an appropriate message.
    """
    global input_correct
    while input_correct is False:
        inp = input("Enter a number between 1-9: \n")
        if not inp.isnumeric() or int(inp) <= 0 or int(inp) > 9:
            print("The input are incorect! Pleas try a number between 1-9")
        elif int(inp) >= 1 and int(inp) <= 9 and board[int(inp)-1] == "-":
            board[int(inp)-1] = player
            input_correct = True
        else:
            print("The spot is alredy taken! Pleas try a number between 1-9")
    input_correct = False


def switchPlayer():
    """
    Switch between player and computer's turn to choose
    """
    global player
    if player == "x":
        player = "o"
    else:
        player = "x"


def computer(board):
    """
    Sets the computer's choices and makes them random
    """
    while player == "o":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "o"
            switchPlayer()


def checkHorizont(board):
    """
    Checks if any player has got three in a row
    horizontally. And if so, that puts the player as the winner
    """
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


def checkVertic(board):
    """
    Checks if any player has got three in a row
    vertically. And if so, that puts the player as the winner
    """
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


def checkDiagon(board):
    """
    Checks if any player has got three in a row
    diagonally. And if so, that puts the player as the winner
    """
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


def checkWinner():
    """
    Check if someone has won. And if someone won, a message will appear
    And the game restarts
    """
    global board
    if checkHorizont(board) or checkVertic(board) or checkDiagon(board):
        displayBoard(board)
        print(f"Winner is {winner}")
        time.sleep(2.4)
        board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]
        restartGame()


def checkTie():
    """
    Check if it's a tie. And if so a message will appear
    And the game restarts.
    """
    global board
    if "-" not in board:
        displayBoard(board)
        print("It,s a tie!")
        board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]
        restartGame()


while gameRunning:
    """
    Calls function in the correct order when the game is running
    """
    refereceBoard(refBoard)
    displayBoard(board)
    playerChoise(board)
    checkWinner()
    checkTie()
    switchPlayer()
    computer(board)
    checkWinner()
    checkTie()
    os.system('clear')
