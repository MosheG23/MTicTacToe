# import
import random

# global variables

board = ["-"]
board_size = 3
amount_of_cells = 0
players = []
number_of_players = 0
turn = 1
amount_to_win = 0

# Customize game variables - touch with care!
smallest_board = 3
biggest_board = 7

# Show Status
def Show_Status():
    print("*************************************")
    print("Current Board:")
    Display_Board()
    print(f"Number of turn: {turn}")

# Play game functions

## Define game setup - size of board, amount of players

def Game_Setup():
    # Greet Players
    print("Hi! Welcome to Tic Tac Toe v2, here you can select the amount of player and the size of the board!")
    print("Have Fun!")
    # Initialize the game
    Board_Initialization()
    Define_Players()
    Decide_Amount_To_Win()

# Setup board
def Board_Initialization():
    global board, board_size, amount_of_cells
    # Select Board Size
    print("*************************************")
    print("Please select the size of board, the number of rows and columns will be the same.", end = " ")
    print(f"The range for acceptable size is from {smallest_board}-{biggest_board}")
    ##### If I want to give the option to choose board size
    board_size = input()
    board_size = Check_Int_Input_And_Range(board_size, f"The range for acceptable size is from {smallest_board}-{biggest_board}: ", smallest_board, biggest_board)
    # Check if input is correct otherwise enter again
    amount_of_cells = board_size * board_size
    board = [""] * board_size
    for i in range(0, board_size):
        board[i] = ["-"] * board_size
    FillBoard()

def FillBoard():
    global board
    count = 1
    for i in range(0, board_size):
        for j in range(0, board_size):
            board[i][j] = count
            count+= 1

# Decide amount to win
def Decide_Amount_To_Win():
    global amount_to_win
    while (amount_to_win == 0):
        if (board_size <= 4):
            amount_to_win = 3
            break;
        elif (board_size <= 6):
            amount_to_win = 4
            break;
        amount_to_win = 5

# Define Players
def Define_Players():
    global players, number_of_players
    playerOptions = ["M", "O", "S", "H", "E", "G", "T"]
    print("*************************************")
    # Amount of players
    if (board_size == 3):
        number_of_players = 2
        print("Amount of players can be only 2!")
    else:
        print("Please select the amount of players, the amount should be between 2 to " + str(board_size - 1))
        numberOfPlayers = input()
        number_of_players = Check_Int_Input_And_Range(numberOfPlayers, "The range is between 2 to " + str(board_size), 2, board_size -1)
    print("*************************************")
    # Select player symbol
    players = [""] * number_of_players
    for i in range(0, number_of_players):
        print(f"Player {i+1}: ")
        print("Which of the available symbols do you want?")
        # Print symbols left to choose
        for j in range(0, len(playerOptions) - 1):
            print(str(j+1) + " - " + playerOptions[j] , end =" ")
        print("")
        playerOption = input()
        playerOption = Check_Int_Input_And_Range(playerOption, "Please Decide again: ", 1 , len(playerOptions)) - 1
        # Print player decsion
        print(f"Player {i+1} --->> " + playerOptions[playerOption])
        players[i] = playerOptions[playerOption]
        # Remove selected symbol, can be selected one once
        playerOptions.pop(playerOption)

## handle turn

def Handle_Turn(currentPlayer, turn):
    global board
    playerSign = players[currentPlayer - 1]
    print(f"Turn {turn}: {playerSign} ({currentPlayer})-")
    # Check if the turn wad done
    putOnBoard = False
    while (putOnBoard == False):
        pos = input(f"Choose position from 1-{amount_of_cells}: ")
        if (int(pos) == 0):
            return;
        pos = Check_Int_Input_And_Range(pos, f"Choose position from 1-{amount_of_cells}: ", 1, amount_of_cells) - 1
        row = int(pos % board_size)
        column = int(pos / board_size)
        # Check if the cell is empty
        if (board[column][row] not in players):
            # Update board
            board[column][row] = playerSign
            putOnBoard = True
        else:
            print("The position is taken. Try again!")
    # Check if there may be a win only if the player played enough turns to win
    if (turn / 2 + 1 > amount_to_win):
        if(Check_Win(playerSign, pos)):
            return True
    return False


############################### Outcome

## Check win
def Check_Win(playerSign, position):
    # playerSign = players[playerNumber - 1]
    if (Check_Rows(playerSign, position) == True):
        print(f"{playerSign} won in row {int(position/2) + 1}")
        return True
    if (Check_Columns(playerSign, position)):
        print(f"{playerSign} won in column {int(position%2) + 1}")
        return True
    print("2")
    return False

######################## To determine the outcome we need to check:
########### Rows, Columns and Diagonal

### check rows
def Check_Rows(playerSign, position):
    row = int(position / board_size)
    for i in range(0, board_size - amount_to_win + 1):
        count = 0
        flag = 0
        while(flag == 0 and i <= board_size - 1 and count <= amount_to_win):
            if (board[row][i] == playerSign):
                count+=1
                i+=1
            else:
                flag = 1
        if (count >= amount_to_win):
            return True
    return False

    return False

### check columns
def Check_Columns(playerSign, position):
    column = int(position % board_size)
    for i in range(0, board_size - amount_to_win + 1):
        count = 0
        flag = 0
        while(flag == 0 and i <= board_size - 1 and count <= amount_to_win):
            if (board[i][column] == playerSign):
                count+=1
                i+=1
            else:
                flag = 1
        if (count >= amount_to_win):
            return True
    return False

### check diagonal
def Check_Diagonal(playerSign, position):
    column = int(position % board_size)
    row = int(position / board_size)
    if(board_size == amount_to_win):
        if (Check_Diagonal_Left(playerSign, 0, amount_to_win - 1) or Check_Diagonal_Right(playerSign, 0, amount_to_win - 1)):
            print(f"Player {playerSign} won with diagonal with position {position}")
            return True
    return False

# How much to check is the size of the board we need to check
def Check_Diagonal_Left(playerSign, start, howMuchToCheck):
    for i in range(start, howMuchToCheck  - amount_to_win + 1):
        count = 0
        flag = 0
        while(flag == 0 and i <= board_size - 1 and count <= amount_to_win):
            if (board[i][i] == playerSign):
                count+=1
                i+=1
            else:
                flag = 1
        if (count >= amount_to_win):
            return True
    return False

def Check_Diagonal_Right(playerSign, start, howMuchToCheck):
    for i in range(start, 0, -1):
        count = 0
        flag = 0
        while(flag == 0 and i <= board_size - 1 and count <= amount_to_win):
            if (board[i][i] == playerSign):
                count+=1
                i-=1
            else:
                flag = 1
        if (count >= amount_to_win):
            return True
    return False


# auxiliary functions - Supporting Functions

############# Calculate ####################
def Get_How_Much(position, case):
    column = int(position % board_size)
    row = int(position / board_size)
    howMuch = []
    # For Rows
    if (case == 1):
        start = row
        # Create board to left
        while (start <= amount_to_win and start >= 0):
            start -= 1
        howMuch.append(start)
        end = row
        # Create board to right
        while (end <= amount_to_win and end <= board_size - 1):
            end += 1
        howMuch.append(end)
        return howMuch;
    # For Columns
    if (case == 2):
        start = column
        # Create board to left
        while (start <= amount_to_win and start >= 0):
            start -= 1
        howMuch.append(start)
        end = column
        # Create board to right
        while (end <= amount_to_win and end <= board_size - 1):
            end += 1
        howMuch.append(end)
        return howMuch;
    # # Create for diagonal
    # Create board for start row, column
    startRow = row
    startCol = column
    while (startRow <= amount_to_win and startRow >= 0 and startCol >= board_size - 1):
        startRow -= 1
        startCol -= 1
    # Create board for start column
    howMuch.append([startRow, startCol])
    # Create board for end row, column
    endRow = row
    endCol = column
    while (endRow <= amount_to_win and endRow <= board_size - 1 and endCol <= board_size - 1):
        endRow += 1
        endCol += 1
    # Create board for end column
    howMuch.append([endRow, endCol])
    return howMuch 

############# Printing ####################
# Display board
def Display_Board():
    print("*************************************")
    print("Current Board:")
    if (amount_of_cells <= 10):
        for i in range(0, board_size):
            for cells in range(0, board_size - 1):
                print(str(board[i][cells]) + " |", end = " ")
            print(str(board[i][board_size - 1]))
    else:
        for i in range(0, board_size):
            for cells in range(0, board_size - 1):
                if (board[i][cells] <= 9):
                    print(" " + str(board[i][cells]) + " |", end = " ")
                    # print("b ", end= " ")
                else:
                    print(str(board[i][cells]) + " |", end = " ")
            if (board[i][cells] <= 9):
                print(" " + str(board[i][board_size - 1]))
            else:
                print(str(board[i][board_size - 1]))

# Check input function for int with range
def Check_Int_Input_And_Range(input_num, message, start, end):
    while (True):
        # Try to convert to integer
        try:
            input_num = int(input_num)
            if (start != end):
                if(input_num <= end and input_num >= start):
                    break;  
                print("Input isn't the range " +str(start) + "-" + str(end))
            else:
                return 1
            input_num = input(message)
        except ValueError:
            try:
                val = float(input_num)
                print("Input is a float  number. Number = ", input_num)
                input_num = input(message)
            except ValueError:
                print("No.. input is not a number. It's a string")
                input_num = input(message)
    return input_num

## Get number of player sign in rows
def Get_Number_Of_Player_In_Row (playerSign, row):
    count = 0
    for i in range(0, board_size - 1):
        if (board[row][i] == playerSign):
            count+=1
    return count

# main

def main():
    global turn
    # Initialize the game
    Game_Setup()
    Display_Board()
    print("Need to win: " + str(amount_to_win))
    # Start Playing
    turn = 1
    # Random first player to start
    startingPlayer = random.randint(1, number_of_players)
    gameStillGoing = True
    while gameStillGoing:
        currentPlayer = (startingPlayer + (turn - 1)) % number_of_players
        print(f"Player {currentPlayer+1}")
        # Handle_Turn(currentPlayer, turn)
        if (turn > amount_of_cells or Handle_Turn(currentPlayer, turn)):
            gameStillGoing = False
        else:
            turn+=1
        Show_Status()
    print("")

if __name__ == "__main__":
    main()