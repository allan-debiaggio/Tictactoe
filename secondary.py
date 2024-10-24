# array = cars = ["Lexus", "Toyota", "Mercedez"]
# append("") is used to add a new element to an existing list/array.
# ex: cars.append("Honda")
# clear()
# ex: cars.clear()
# copy()
# include in variable
# count("") - count the number of occurrences of the element


board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

player = "X", "O"
winner = None


def array():
    for i in range (3):
        print(" ".join (board [i]))

def x(b, c):
    board [b][c] = "X"
def y(b, c):
    board [b][c] = "O"


row= int(input("Enter a row from 0 - 2: "))
column= int(input("Enter a column from 0 - 2: "))

x(row, column)
if x == "-":
    x(row, column)
else: 
    print("Invalid")


y(row, column)
if y == "-":
    y(row, column)
else:
    print("Invalid")

array()