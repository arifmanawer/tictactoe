# Game Step
# get user input

player1Mark = input("Please choose X or O: ")
choices = ["X", "O"]
if player1Mark not in choices:
    while player1Mark not in choices:
        player1Mark = input("Please enter valid choice. (X or O) ")
if player1Mark == "X":
    player2Mark = "O"
else:
    player2Mark = "X"

board = []
for row in range(3):
    board.append([""] * 3)

for row in range(3):
    print(board[row])


def checkIfMoveValid(row, col):
    if not (row >= 0 and row < 3 and col >= 0 and col < 3):
        return False
    if (board[row][col] == ""):
        return True


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
                # checks is the entire row is the same which would be a win for the player
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
    if board[row][column] == "":
        return False

    currentMatch = 1
    for i in range(2):
        row += increment
        column += increment
        if board[row][column] == mark:
            currentMatch += 1
    if currentMatch == 3:
        return True
    return False


def checkDiagonalWin():
    if checkDiagonal(0, 0, 1) or checkDiagonal(0, 2, -1) == True:
        return True
    else:
        return False


def checkForWinner():
    return checkVertialWin() or checkDiagonalWin() or checkHorizontalWin


def isBoardFull():
    for row in range(3):
        for column in range(3):
            if board[row][column] == "":
                return False
    return True


def ticTacToe():
    while True:
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
