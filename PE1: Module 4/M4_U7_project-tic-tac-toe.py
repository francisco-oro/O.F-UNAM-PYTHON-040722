import random as random
def DisplayBoard(board):
    #This function accepts a parameter that stores the current state of the board and shows it to console
    for row in range(3):
        print("+-------+-------+-------+", "|       |       |       |", "|   %s   |   %s   |   %s   |" \
            % (board[row][0], board [row][1], board[row][2]), "|       |       |       |", sep ="\n")
    print("+-------+-------+-------+")

def EnterMove(board):
    #This function accepts the current state of the board and asks the user about its movement, 
    #Verifies te input and updates the board accordingly to the user's input
    reservedChars = ('X', 'O')
    isOver = False
    while(not isOver):
        try:
            newMove = int(input("Choose your movement: "))
            newMove -= 1
            if newMove not in range(9):
                print(newMove + 1, "is not a valid movement")
                continue
            if newMove in range(3):
                if board[0][newMove] not in reservedChars:
                    board[0][newMove] = 'O'
                    isOver = True
                    continue
                else: 
                    print("Sorry, this cell has already been choosen")
                    continue
            elif newMove in range(6):
                if board[1][newMove - 3] not in reservedChars:
                    board[1][newMove - 3] = 'O'
                    isOver = True
                    continue
                else: 
                    print("Sorry, this cell has already been choosen")
                    continue
            else:
                if board[2][newMove - 6] not in reservedChars:
                    board[2][newMove - 6] = 'O'
                    isOver = True
                    continue
                else: 
                    print("Sorry, this cell has already been choosen")
                    continue
        except:
            print("not a valid input")
    return board
    
def MakeListOfFreeFields(board):
    # This function examines the gameboard and builds a list of all the empty cells
    # The list is made up of tuples, where every tuple is a pair of elements that represent the row and column.
    reservedChars = ('X', 'O')
    emptyCells = []
    for i in range(3): 
        for j in range(3):
            if board[i][j] in reservedChars: continue
            emptyCells.append((i, j))
    return emptyCells

def VictoryFor(board, sign):
    #This function analyses the gameboard status to find out whether the player using the O's or the X's has won the game.
    #Row inspection
    n = 2 #column control
    results = [0 for x in range(4)] #['rowCounter', 'columnCounter', 'diagCounter', 'reverseDiagCounter']
    winner = False
    for i in range(3):
        results[0] = results[1] = 0
        if board[i][n] == sign: results[3] += 1
        if board[i][i] == sign: results[2] += 1 
        n -= 1
        for j in range(3): 
            if board[i][j] == sign: results[0] += 1
            if board[j][i] == sign: results[1]+= 1
            if 3 in results: 
                winner = True
                return winner
    print(results, sign)
    return winner

def DrawMove(board, emptyCells):
    # This function draws in the movement of the machine and updates the gameboard. 
    newMove = (random.choice(emptyCells))
    board[newMove[0]][newMove[1]] = 'X'
    return board

print("TIC-TAC-TOE \nDeveloped by: Francisco Abimael Oro Estrada")
playerName = input("What's your name? ")
print("Welcome,", playerName)
isOver = False
playerScore = pcScore = 0
while(not isOver):
    print("Current scores: %s - %d, computer - %d" %(playerName, playerScore, pcScore))
    board =[[str(n) for n in range(1, 4)],['4', 'X', '6'], [str(n) for n in range(7, 10)]]
    DisplayBoard(board)
    while(True):
        board = EnterMove(board)
        if VictoryFor(board, "O"):
            print(playerName, "has won!")
            playerScore += 1
            break
        DisplayBoard(board)
        emptyCells = MakeListOfFreeFields(board)
        DrawMove(board, emptyCells)
        DisplayBoard(board)
        emptyCells = MakeListOfFreeFields(board)
        if VictoryFor(board, "X"): 
            print("Computer has won!")
            pcScore += 1 
            break
        if len(emptyCells) == 0:
            print("Draw")
            break
    isOver = True if input("Wanna play again [y, n]") == 'n' else False