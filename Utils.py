from os import system, name
from copy import deepcopy


def clearScreen():
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')


def printBoard(board):

    print("\n")

    print(board[0] + "(00)----------------------" + board[1] + "(01)----------------------" + board[2] + "(02)")
    print("| \                         |                         / |")
    print("|   \                       |                       /   |")
    print("|     \                     |                     /     |")
    print("|       " + board[3] + "(03)--------------" + board[4] + "(04)--------------" + board[5] + "(05)     |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |        " + board[6] + "(06)-----" + board[7] + "(07)-----" + board[8] + "(08)       |      |")
    print("|       |         |         |         |          |      |")
    print("|       |         |         |         |          |      |")
    print("|       |         |         |         |          |      |")
    print(board[9] + "(09)---" + board[10] + "(10)----" + board[11] + "(11)-----"+ board[12] + "(12)-----" + board[13] + "(13)----" + board[14] + "(14)---" + board[15] + "(15)")
    print("|       |         |         |         |          |      |")
    print("|       |         |         |         |          |      |")
    print("|       |         |         |         |          |      |")
    print("|       |        " + board[16] + "(16)-----" + board[17] + "(17)-----" + board[18] + "(18)       |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       " + board[19] + "(19)--------------" + board[20] + "(20)--------------" + board[21] + "(21)     |")
    print("|     /                     |                     \     |")
    print("|   /                       |                       \   |")
    print("| /                         |                         \ |")
    print(board[22] + "(22)----------------------" + board[23] + "(23)----------------------" + board[24] + "(24)")
    print("\n")

def adjacentlocations(position):
    adjacent=[
        [1,3,9],
        [0,2,3,4,5],
        [1,5,15],
        [0,10,4],
        [1,3,5,7],
        [4,2,14],
        [7,11],
        [4,6,8,12],
        [7,13,],
        [0,22,10],
        [3,9,11,19],
        [6,10,12,16],
        [7,11,13,17],
        [8,12,14,18],
        [5,13,15,21],
        [2,14,24],
        [11,17],
        [12,16,18,20],
        [13,17],
        [10,20,22],
        [17,19,21,23],
        [14,20,24],
        [9,19,23],
        [20,22,24],
        [15,21,23]
    ]
    return adjacent[position]

#Check piece is present in adjacent positions
def existingPiece(player,board,pos1,pos2):
    if (board[pos1] == player and board[pos2] == player):
        return True
    else:
        return False


# Return True if a player has a mill on the given position
# Each position has an index
def checkMill(position, board):
    p = board[position]
    # The player on that position
    if p != 'x':
        # If there is some player on that position
        return checkNextMill(position, board, p)
    else:
        return False

# Function to check if a player can make a mill in the next move.
# Return True if the player can create a mill
def checkNextMill(position, board, player):
    mill = [
        (existingPiece(player, board, 1, 2) or existingPiece(player, board, 3, 5)),
        (existingPiece(player, board, 0, 2) or existingPiece(player, board, 9, 17)),
        (existingPiece(player, board, 0, 1) or existingPiece(player, board, 4, 7)),
        (existingPiece(player, board, 0, 5) or existingPiece(player, board, 11, 19)),
        (existingPiece(player, board, 2, 7) or existingPiece(player, board, 12, 20)),
        (existingPiece(player, board, 0, 3) or existingPiece(player, board, 6, 7)),
        (existingPiece(player, board, 5, 7) or existingPiece(player, board, 14, 22)),
        (existingPiece(player, board, 2, 4) or existingPiece(player, board, 5, 6)),
        (existingPiece(player, board, 9, 10) or existingPiece(player, board, 11, 13)),
        (existingPiece(player, board, 8, 10) or existingPiece(player, board, 1, 17)),
        (existingPiece(player, board, 8, 9) or existingPiece(player, board, 12, 15)),
        (existingPiece(player, board, 3, 19) or existingPiece(player, board, 8, 13)),
        (existingPiece(player, board, 20, 4) or existingPiece(player, board, 10, 15)),
        (existingPiece(player, board, 8, 11) or existingPiece(player, board, 14, 15)),
        (existingPiece(player, board, 13, 15) or existingPiece(player, board, 6, 22)),
        (existingPiece(player, board, 13, 14) or existingPiece(player, board, 10, 12)),
        (existingPiece(player, board, 17, 18) or existingPiece(player, board, 19, 21)),
        (existingPiece(player, board, 1, 9) or existingPiece(player, board, 16, 18)),
        (existingPiece(player, board, 16, 17) or existingPiece(player, board, 20, 23)),
        (existingPiece(player, board, 16, 21) or existingPiece(player, board, 3, 11)),
        (existingPiece(player, board, 12, 4) or existingPiece(player, board, 18, 23)),
        (existingPiece(player, board, 16, 19) or existingPiece(player, board, 22, 23)),
        (existingPiece(player, board, 6, 14) or existingPiece(player, board, 21, 23)),
        (existingPiece(player, board, 18, 20) or existingPiece(player, board, 21, 22))
    ]
    return mill[position]


# Function to return number of pieces owned by a player on the board.
# value is '1' or '2' (player number)
def numOfPieces(board, value):
    return board.count(value)