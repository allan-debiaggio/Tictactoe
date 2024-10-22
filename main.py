# Function to print the Tic-Tac-Toe board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if any player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (draw)
def check_draw(board):
    return ' ' not in board

# Main function to play the game
def play_game():
    # Initialize empty board
    board = [' ' for _ in range(9)]
    current_player = 'X'  # Player 'X' goes first
    
    while True:
        print_board(board)
        
        # Get input from the current player
        move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
        
        # Check if the position is valid
        if board[move] != ' ':
            print("Invalid move, try again.")
            continue
        
        # Place the player's mark on the board
        board[move] = current_player
        
        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    play_game()
