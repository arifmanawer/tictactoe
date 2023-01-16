# Game Step
# get user input

player1Mark = input("Please choose X or O: ")  # sets players mark
choices = ["X", "O"]
if player1Mark not in choices:
    while player1Mark not in choices:  # loops until player picks a valid mark
        player1Mark = input("Please enter valid choice. (X or O) ")
if player1Mark == "X":
    player2Mark = "O"
else:
    player2Mark = "X"

board = []  # makes the 3x3 board
for row in range(3):
    board.append([""] * 3)
for row in range(3):
    print(board[row])


def checkIfMoveValid(row, col):  # checks if the players move is valid
    if not (row >= 0 and row < 3 and col >= 0 and col < 3):
        return False
    # returns true if the square the player picked is empty and allowed to move there
    return board[row][col] == ""


def playerMoves(mark):
    validMove = False

    while not validMove:  # loop continues until validmove is true which means user picked a valid move
        moveRow = int(input("Please pick a row: "))
        moveCol = int(input("Please pick a column: "))
        validMove = checkIfMoveValid(moveRow, moveCol)
        if not validMove:
            print("Please enter a valid move.")

    board[moveRow][moveCol] = mark  # sets the square as the players mark


def checkHorizontalWin():
    for row in range(3):
        currentMark = board[row][0]
        if currentMark == "":  # checks if the square is empty
            continue

        currentMatches = 1
        for column in range(1, 3):
            if currentMark == board[row][column]:
                # checks if the entire row is the same which would be a win for the player
                currentMatches += 1

        if currentMatches == 3:
            return True
    return False


def checkVertialWin():
    for column in range(3):
        currentMark = board[0][column]
        if currentMark == "":
            continue

        currentMatches = 1
        for row in range(1, 3):
            if currentMark == board[row][column]:
                currentMatches += 1  # checks if the entire column is the same

        if currentMatches == 3:
            return True

    return False


def checkDiagonal(row, column, increment):
    mark = board[row][column]
    if mark == "":
        return False

    currentMatch = 1
    for i in range(2):  # checks to see if there is a diagonal win by comparing top corner squares and incrementing
        # to see middle and opposite corners
        row += increment
        column += increment
        if mark == board[row][column]:
            currentMatch += 1
    if currentMatch == 3:
        return True
    return False


def checkDiagonalWin():
    return checkDiagonal(0, 0, 1) or checkDiagonal(0, 2, -1)


def checkForWinner():  # checks for win based on the 3 possible ways to win
    return checkVertialWin() or checkDiagonalWin() or checkHorizontalWin()


def isBoardFull():  # loops through board after maximum moves to see if the board is full
    for row in range(3):
        for column in range(3):
            if board[row][column] == "":
                return False
    return True


def ticTacToe():
    while True:  # loop continues until a player wins or the board is full
        # switches between both players after each move
        for mark in [player1Mark, player2Mark]:
            playerMoves(mark)
            for row in range(3):
                print(board[row])

            if checkForWinner():
                print(mark, " wins!")
                return

            if isBoardFull():
                print("Game over! No one won.")
                return


ticTacToe()
