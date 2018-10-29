#!/usr/bin/python
# # Usage: python chessercise.py --piece KNIGHT --inputPosition d2
# Author: Divyapuja Vitonde
#
# Assumptions:
# A board is of sixe 8X8.
# When a piece type and input position is entered to run the program, there are no other pieces on the board.
#
import sys
 
# Find possible moves for a given piece
def findPossibleMoves(piece, pos1, pos2):
    if piece == 'KNIGHT':
        moves = knightMoves(pos1, pos2)
    elif piece =='ROOK':
        moves = rookMoves(pos1, pos2)
    elif piece == 'QUEEN':
        moves = queenMoves(pos1, pos2)
    return moves


# Get all right moves for rook/queen
def goRight(fromColumn,fromRow):
    moves =[]
    for i in range(N,fromColumn, -1):
        if i in numberToAlphabet:
                movePos = str(fromRow)+str(numberToAlphabet[i])
                moves.append(movePos)
    return moves

# Get all left moves for rook/queen
def  goLeft(fromColumn,fromRow):
    moves =[]
    for i in range(1,fromColumn):
        if i in numberToAlphabet:
                movePos = str(fromRow)+str(numberToAlphabet[i])
                moves.append(movePos)
    return moves

# Get all upwards moves for rook/queen
def goUp(fromColumn,fromRow):
    moves =[]
    for i in range(fromRow+1,N+1):
        if i in numberToAlphabet:
                movePos = str(i)+str(numberToAlphabet[fromColumn])
                moves.append(movePos)
    return moves

# Get all downwards moves for rook/queen
def goDown(fromColumn,fromRow):
    moves =[]
    for i in range(fromRow-1,0,-1):
        if i in numberToAlphabet:
            movePos = str(i)+str(numberToAlphabet[fromColumn])
            moves.append(movePos)
    return moves


# Get all north east moves for queen
def goNorthEast(fromColumn,fromRow,toRight, toUp):
    moves =[]
    if toRight < toUp:
        for i in range(fromColumn+1,N+1):
            if i in numberToAlphabet:
                fromColumn =fromColumn +1
                fromRow=fromRow+1
                movePos = str(fromRow)+str(numberToAlphabet[fromColumn])
                moves.append(movePos)
    if toUp < toRight: 
        for i in range(fromRow,N):
            if i in numberToAlphabet:
                fromColumn = fromColumn +1
                fromRow = fromRow+1
                movePos = str(fromRow)+str(numberToAlphabet[fromColumn])
                moves.append(movePos)
    if toRight == toUp:
        for i in range(fromRow,N):
            if i in numberToAlphabet:
                j = i+1
                movePos = str(j) + str(numberToAlphabet[j])
                moves.append(movePos)
    return moves

# Get all south east moves for queen
def goSouthEast(fromColumn,fromRow):
    moves =[]
    for i in range(fromRow-1,0,-1):
        if i in numberToAlphabet:
            fromColumn = fromColumn +1
            fromRow=fromRow-1
            if fromColumn<N+1 and fromRow>0:
                movePos = str(fromRow)+str(numberToAlphabet[fromColumn])
                moves.append(movePos)
    return moves

# Get all south west moves for queen
def goSouthWest(fromColumn,fromRow):
    moves =[]
    for i in range(fromRow-1,0,-1):
        if i in numberToAlphabet:
            fromColumn = fromColumn -1
            fromRow=fromRow-1
            if fromColumn>0 and fromRow >0:
                movePos = str(fromRow) + str(numberToAlphabet[fromColumn])
                moves.append(movePos)
    return moves

# Get all north west moves for queen
def goNorthWest(fromColumn,fromRow):
    moves =[]
    for i in range(fromRow+1,N+1):
        if i in numberToAlphabet:
            fromColumn = fromColumn -1
            fromRow=fromRow+1
            if fromColumn>0 and fromRow < N+1:
                movePos = str(fromRow) + str(numberToAlphabet[fromColumn])
                moves.append(movePos)
    return moves


# Get all moves for rook
def rookMoves(fromColumn, fromRow):
    return goRight(fromColumn,fromRow) + goLeft(fromColumn,fromRow) + goUp(fromColumn,fromRow) + goDown(fromColumn,fromRow)


# Get all moves for knight
def knightMoves(p, q):
    #All possible moves of a knight 
    X = [ 2, 1, -1, -2, -2, -1, 1, 2 ]; 
    Y = [ 1, 2, 2, 1, -1, -2, -2, -1 ]; 
    moves = []
    arr = []
    for i in range(1,N+1):
        x = p + X[i-1]
        y = q + Y[i-1]
        if y>0 and y < N+1:
            if x in numberToAlphabet:
                movePos = str(y)+str(numberToAlphabet[x])
                moves.append(movePos)
    return moves


# Get all moves for queen
def queenMoves(fromColumn, fromRow):
    toRight = N - fromColumn
    toUp = N - fromRow
    moves = rookMoves(fromColumn, fromRow) + goNorthEast(fromColumn, fromRow, toRight, toUp) + goSouthEast(fromColumn, fromRow) + goSouthWest(fromColumn, fromRow) + goNorthWest(fromColumn, fromRow) 
    #print(moves)
    return moves

# print the moves
def printMoves(moves):
    moves.sort()
    allMoves = []
    for i in sorted(moves):
        allMoves.append(i[1]+i[0])
    return ',' .join(allMoves)


'''
Accepts user input, validates the input, finds the possibe moves for the piece and finally prints the moves 
'''
def main():
    # Get the arguments list 
    inputArgs = sys.argv
    validPieces = ['QUEEN', 'ROOK', 'KNIGHT']
    piece = inputArgs[2]
    inputPosition = inputArgs[4]

    if piece.upper() not in validPieces:
        raise ValueError('Invalid piece')  

    pos2 = int(inputPosition[1:len(inputPosition)])
    if pos2<1 or pos2>N:
        raise ValueError('Invalid location')  

    pos1=''
    posZero = inputPosition[0].lower()

    if posZero in alpbabetToNumber:
        # Get numberic position for alphabet
        pos1 = alpbabetToNumber[posZero]
    else:
        raise ValueError('Invalid location')  
    
    moves = findPossibleMoves(piece, pos1, pos2)
    
    print(printMoves(moves))


# Program execution starts here
# Assumption: The board is of size 8X8
N = 8
# Since the input location will contain characters from a-h, this dictionary object is used to map alpbabets to number 
alpbabetToNumber = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
# and , below dictionary is used to reverse map numbers to alphabets
numberToAlphabet = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}
# call the main function
main()
