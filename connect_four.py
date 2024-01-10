#Takes the board as an input and prints it out in a grid manner
def print_board(board):
   for row in board:
        for col in row:
           print(col , end = '')
        print()

#Creates the board as a grid
def initialize_board(num_rows,num_cols):
   board = []
   board_str= ''
   for rows in range(num_rows):
       #Creates a list in a list
       board.append([])
       #Adds the correct amount of columns in each list
       for col in range(num_cols):
           board[rows].append("-")
   return board

def insert_chip(board, col, chip_type):
    #Inserts the chip in the last row slot
    row = -1
    col = int(col)
    #If the slot is taken it goes to the 2nd to last row slot, and if thats taken that it goes to 3rd ...
    while board[row][col] == 'x' or board[row][col] == 'o':
       row -= 1
    board[row][col] = chip_type
    print_board(board)
    return col,row

def check_if_winner(board, col, row, chip_type):
    #To get num_cols defined within the function
    num_cols= len(board[0])
    #Checks each row in the same column spot to see if 4 chips are connected
    if board[row][col] == board[row+1][col]:
        if board[row+1][col] == board[row+2][col]:
            if board[row+3][col] == board[row+2][col]:
                if chip_type == board[row+3][col]:
                    return True
    #Checks the entire row of the last placed chip and returns True if any 4 are connected
    for i in range(num_cols):
            if board[row][i] == board[row][i-1]:
                if board[row][i-1] == board[row][i-2]:
                    if board[row][i-2] == board[row][i-3]:
                        if chip_type == board[row][i-3]:
                            return True
    #Checks if the board is filled with either x's or o's and returns 3 so it is different then winning from horizontal or vertical
    if all(chip in ('x', 'o')
           for row in board
           for chip in row):
                print('Draw. Nobody wins.')
                return 3
    else:
        return False


if __name__ == "__main__":

    num_rows = int(input("What would you like the height of the board to be? "))
    num_cols = int(input("What would you like the length of the board to be? "))
    count = 0
    #Defined the board to the function
    board = initialize_board(num_rows,num_cols)
    print_board(board)
    print("Player 1: x")
    print("Player 2: o\n")
    while True:
        col = input("Player 1: Which column would you like to choose? ")
        col, row = insert_chip(board, col, 'x')
        #Checks for draw
        if check_if_winner(board, col, row, chip_type='x') == 3:
            break
        #Checks for a win
        if check_if_winner(board, col, row, 'x'):
            print("Player 1 won the game! ")
            break
        col = input("Player 2: Which column would you like to choose? ")
        col, row = insert_chip(board, col, 'o')
        if check_if_winner(board, col, row, chip_type='o') == 3:
            break
        if check_if_winner(board, col, row, 'o'):
            print("Player 2 won the game! ")
            break
