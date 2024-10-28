# Day 7 TicTacToe - with List
# Need to use "try" and "except" for value errors (program will not crash if provided something else than int)
# Need to make a function for winning / losing / draw
# Need to make a bot or AI, or both
# Presentation :
# Make slides
# Demonstrate
# Explain code
# Improvements
# Questions
import random
grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]  # Grid "tutorial" for numbers by user

def print_grid(a):
    print(a[0:3])
    print(a[3:6])
    print(a[6:9])

print("Welcome to TicTacToe!")
print_grid(grid)

grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # Grid reset

# Winning Conditions

def check_winner():
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if grid[combo[0]] == grid[combo[1]] == grid[combo[2]] != " ":
            return grid[combo[0]]
    if " " not in grid:
        return "Draw"
    return None

def player1():  # Player 1 function with loop and conditions for user input
    while True:
        try:
            a = int(input("Player 1, give a number corresponding to the grid to play: "))
            if a < 1 or a > 9 or grid[a - 1] != " ":
                print("Player 1, please give a CORRECT UNUSED INTEGER number corresponding to the grid to play.")
                continue
        except ValueError:  # Handling non-integers input
            print("Give an integer please.")
            continue
        grid[a - 1] = "O"
        print_grid(grid)
        return a

def player2():  # Player 2 function with loop and conditions for user input
    while True:
        try:
            b = int(input("Player 2, give a number corresponding to the grid to play: "))
            if b < 1 or b > 9 or grid[b - 1] != " ":
                print("Player 2, please give a CORRECT UNUSED number corresponding to the grid to play.")
                continue
        except ValueError:  # Handling non-integers input
            print("Give an integer please.")
            continue
        grid[b - 1] = "X"
        print_grid(grid)
        return b

def bot():
    while True :
        c = random.randrange(1,10)
        if grid[c-1] != " ":
            c = random.randrange(1,10)
        else :
            print("The bot took its turn !")
            grid[c-1] = "X"
            print_grid(grid)
            return c
        
# Game select & infinite Loop that checks for player turns & winner check
game_select = int(input("Choose a game mode : 1 for PvP, 2 for PvE : "))
if game_select == 1 :
    while True:
        player1()
        winner = check_winner()
        if winner:
            if winner == "Draw":
                print("This is a draw... Try again!")
            else:
                print(f"Player {1 if winner == 'O' else 2} wins! Congratulations!")
            break

        player2()
        winner = check_winner()
        if winner:
            if winner == "Draw":
                print("This is a draw... Try again!")
            else:
                print(f"Player {1 if winner == 'O' else 2} wins! Congratulations!")
            break
else :
    while True:
        player1()
        winner = check_winner()
        if winner:
            if winner == "Draw":
                print("This is a draw... Try again!")
            else:
                print(f"Player {1 if winner == 'O' else "bot"} wins! Congratulations!")
            break
        bot()
        winner = check_winner()
        if winner:
            if winner == "Draw":
                print("This is a draw... Try again!")
            else:
                print(f"Player {1 if winner == 'O' else "bot"} wins! Congratulations!")
            break