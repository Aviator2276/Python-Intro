import random
def createBoard():
    global row1
    global row2
    global row3
    global row4
    global row5
    global row6
    global board
    row1 = [" ", " ", " ", " ", " ", " "]
    row2 = [" ", " ", " ", " ", " ", " "]
    row3 = [" ", " ", " ", " ", " ", " "]
    row4 = [" ", " ", " ", " ", " ", " "]
    row5 = [" ", " ", " ", " ", " ", " "]
    row6 = [" ", " ", " ", " ", " ", " "]
    board = [row1, row2, row3, row4, row5, row6]

def placeShip(row, col):
    if row >= 0 and row <= 5 and col >= 0 and col <= 5:
        board[row][col] = "O"
    else:
        print("PLACEMENT FAILED, COORDS AT: " + str(row) + ", " + str(col))

def getFormat():
    formatBoard = ""
    rowPos = 0
    colPos = 0
    for row in board:
        for col in row:
            formatBoard += "+-"
        formatBoard += "+\n"
        for col in row:
            formatBoard += "|"
            if board[rowPos][colPos] == "O":
                formatBoard += " "
            else:
                formatBoard += str(board[rowPos][colPos])
            colPos += 1
        formatBoard += "|\n"
        colPos = 0
        rowPos += 1
    for col in row:
        formatBoard += "+-"
    formatBoard += "+\n"
    return formatBoard

def generateShip1():
    shipX = random.randint(1,4)
    shipY = random.randint(1,4)
    direction = random.randint(0, 1)
    if direction == 0:
        placeShip(shipX, shipY)
        placeShip(shipX+1, shipY)
        placeShip(shipX-1, shipY)
    if direction == 1:
        placeShip(shipX, shipY)
        placeShip(shipX, shipY+1)
        placeShip(shipX, shipY-1)

def checkHit(row, col):
    if board[row][col] == "O" or board[row][col] == "X":
        print("HIT")
        board[row][col] = "X"
    else:
        board[row][col] = "0"
        print("MISS")

def checkWin():
    count = 0
    rPos = 0
    cPos = 0
    for row in board:
        for col in row1:
            if board[rPos][cPos] == "X":
                count += 1
            cPos += 1
        cPos = 0
        rPos += 1
    if count > 2:
        print("YOU SUNK THE SHIP!!!")
        return True
    else:
        return False

createBoard()
checkWin()
generateShip1()
print(getFormat())
while checkWin() == False:
    checkWin()
    posX = input("Set the X coordinate to shoot at (1-6): ")
    posY = input("Set the Y coordinate to shoot at (1-6): ")
    posX = int(posX)
    posY = int(posY)
    if posX >= 1 and posX <=6 and posY >= 1 and posY <=6:
        checkHit(int(posX)-1,int(posY)-1)
        print(getFormat())
    else:
        print("ERROR: Try again with proper syntax")
exit()