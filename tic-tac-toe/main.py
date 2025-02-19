# Explicitly defining a 3x3 two-dimensional array for the Tic-Tac-Toe board
board = [
    [" ", " ", " "],  # Row 1
    [" ", " ", " "],  # Row 2
    [" ", " ", " "]  # Row 3
]


# Example of printing the board to visualize it
def print_board(board):
    print("\n")
    for row in range(3):
        print(" | ".join(board[row]))
        if row < 2:
            print("---------")
    print("\n")


# Print the initial empty board

print_board(board)
game_is_on = True
current_player = 1


def check_winning(board):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            print(f"Player {board[i][0]} has won")
            return True

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != " ":
            print(f"Player {board[0][i]} has won")
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        print(f"Player {board[0][0]} has won")
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        print(f"Player {board[0][2]} has won")
        return True

    return False


while game_is_on:
    print(f"Player {current_player}")

    # Get user input for row and column
    row = int(input("Enter row (0, 1, 2): "))
    col = int(input("Enter column (0, 1, 2): "))
    if board[row][col] == " ":
        # Place the player's mark
        board[row][col] = 'X' if current_player == 1 else 'O'
        print_board(board)
        if check_winning(board):
            game_is_on = False
            # Switch players
        current_player = 2 if current_player == 1 else 1
    else:
        print("Cell already taken. Choose another.")
