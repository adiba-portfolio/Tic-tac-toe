def print_board(board):
    """
    Display the current state of the Tic-Tac-Toe board.
    """
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    """
    Check if there's a winner or if the game is a draw.
    Returns 'X', 'O', 'Draw', or None.
    """
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]  # Row win
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]  # Column win

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]  # Main diagonal win
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]  # Anti-diagonal win

    # Check for a draw (no empty spaces left)
    if all(cell != " " for row in board for cell in row):
        return "Draw"

    return None  # No winner yet


def tic_tac_toe():
    """
    Main function to play a two-player Tic-Tac-Toe game.
    """
    # Initialize an empty 3x3 board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        print(f"Player {players[current_player]}'s turn.")

        # Get the player's move
        try:
            row, col = map(int, input("Enter your move (row and column: 0, 1, or 2 separated by space): ").split())
            if board[row][col] != " ":
                print("Invalid move! Cell is already occupied. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter two numbers between 0 and 2 separated by space. Try again.")
            continue

        # Make the move
        board[row][col] = players[current_player]
        print_board(board)

        # Check for a winner
        result = check_winner(board)
        if result:
            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"Player {result} wins!")
            break

        # Switch players
        current_player = 1 - current_player


if __name__ == "__main__":
    tic_tac_toe()
