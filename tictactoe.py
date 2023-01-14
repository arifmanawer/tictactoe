# Game Step
# get user input

player1Mark = input("Please choose X or O: ")
choices = ["X", "O"]
if player1Mark not in choices:
    while player1Mark not in choices:
        player1Mark = input("Please enter valid choice. (X or O) ")
if player1Mark == "X":
    player2mark = "O"
else:
    player2mark = "X"

board = []
for row in range(3):
    board.append([""] * 3)
for row in range(3):
    print(board[row])
