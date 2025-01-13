#!/usr/bin/python3

def print_board(board):
    """
    Prints the game board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner.
    
    Returns True if there is a winner, otherwise False.
    """
    # Check rows for winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """
    Checks if the game is a draw (board is full and no winner).
    
    Returns True if it's a draw, otherwise False.
    """
    for row in board:
        if " " in row:
            return False  # There is still space, so it's not a draw
    return True  # No space left, it's a draw

def tic_tac_toe():
    """
    Main game loop for Tic Tac Toe.
    Alternates between players X and O until there's a winner or a draw.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Get valid user input for row and column
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                
                if row not in range(3) or col not in range(3):
                    print("Invalid input! Please enter row and column as 0, 1, or 2.")
                elif board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    break  # Valid input, break out of loop
            except ValueError:
                print("Invalid input! Please enter integer values for row and column.")

        # Place the player's mark on the board
        board[row][col] = player

        # Check if the current player has won
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch to the other player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
