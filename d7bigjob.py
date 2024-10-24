#Day 7 TicTacToe - with List
#Need to use "try" and "except" for value errors (program will not crash if provided something else than int)
#Need to make a function for winning / losing / draw
#Need to make a bot or AI, or both
#Presentation :
#Make slides
#Demonstrate
#Explain code
#Improvements
#Questions


grid=["1","2","3","4","5","6","7","8","9"] #Grid "tutorial" for numbers by user
isOver = False

def print_grid(a):
    print(a[0:3])
    print(a[3:6])
    print(a[6:9])

print("Welcome to TicTacToe !")
print_grid(grid)

grid=[" ", " ", " ", " ", " ", " ", " "," ", " "] #Grid reset

def player1 (): #Player 1 function with loop and conditions for user input
    while True :
        try :
            a=int(input("Player 1, give a number corresponding to the grid to play : "))
            while a < 1 or a > 9 or grid[a-1] != " " :
                a=int(input("Player 1, please give a CORRECT UNUSED INTEGER number corresponding to the grid to play : "))
        except(ValueError) : #Handling non-integers input
            a=input("Give an integer please :")
            a=int(a)
        grid[a-1] = "O"
        print_grid(grid)
        return a

def player2 (): #Player 2 function with loop and conditions for user input
    while True :
        try :
            b=int(input("Player 2, give a number corresponding to the grid to play : "))
            while b < 1 or b > 9 or grid[b-1] != " ":
                b=int(input("Player 2, please give a CORRECT UNUSED number corresponding to the grid to play : "))
        except(ValueError) : #Handling non integers input
            b = input("Give an integer please : ")
            b = int(b)
        grid[b-1] = "X"
        print_grid(grid)
        return b

def game_over() : #Winning conditions
        if grid[0:3] or grid[3:6] or grid[6:9] == "O" :
            isOver=True
            print("Player 1 wins ! Congratulations !")
        print("Player 2 wins ! Congratulations !")
        print("This is a draw... Try again !")
    
while isOver == False :
        player1()
        player2()