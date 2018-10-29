#!/usr/bin/python
# Usage
# pip install coverage
# coverage run test_chessercise.py --piece KNIGHT --position d2
# coverage run test_chessercise.py --piece ROOK --position d2
# coverage run test_chessercise.py --piece QUEEN --position d2
# coverage html
from chessercise import *

def test_findPossibleMovesKnight():
    assert findPossibleMoves('KNIGHT', 4, 2) == ['3f', '4e', '4c', '3b', '1b', '1f']
    assert findPossibleMoves('ROOK', 4, 2) == ['2h', '2g', '2f', '2e', '2a', '2b', '2c', '3d', '4d', '5d', '6d', '7d', '8d', '1d']
    assert findPossibleMoves('QUEEN', 4, 2) == ['2h', '2g', '2f', '2e', '2a', '2b', '2c', '3d', '4d', '5d', '6d', '7d', '8d', '1d', '3e', '4f', '5g', '6h', '1e', '1c', '3c', '4b', '5a']

def test_rookMoves():
    assert rookMoves(4 ,4) == ['4h', '4g', '4f', '4e', '4a', '4b', '4c', '5d', '6d', '7d', '8d', '3d', '2d', '1d']

def test_knightMoves():
    assert knightMoves(4 ,4) == ['5f', '6e', '6c', '5b', '3b', '2c', '2e', '3f']

def test_queenMoves():
    assert queenMoves(4 ,4) == ['4h', '4g', '4f', '4e', '4a', '4b', '4c', '5d', '6d', '7d', '8d', '3d', '2d', '1d', '5e', '6f', '7g', '8h', '3e', '2f', '1g', '3c', '2b', '1a', '5c', '6b', '7a']

def test_goNorthEast():
    assert goNorthEast(4 ,2, 4 ,6) == ['3e', '4f', '5g', '6h']
    assert goNorthEast(4 ,4, 4 ,4) == ['5e', '6f', '7g', '8h']
    assert goNorthEast(1,7, 7 ,1) == ['8b']

def test_goSouthEast():
    assert goSouthEast(4 ,4) == ['3e', '2f', '1g']

def test_goSouthWest():
    assert goSouthWest(4 ,4) == ['3c', '2b', '1a']

def test_goNorthWest():
    assert goNorthWest(4 ,4) == ['5c', '6b', '7a']

def test_printMoves():
    assert printMoves(['5c', '6b', '7a']) == 'c5,b6,a7'

def test_goRight():
    assert goRight(4 ,4) == ['4h', '4g', '4f', '4e']

def test_goleft():
    assert goLeft(4 ,4) == ['4a', '4b', '4c']

def test_goUp():
    assert goUp(4 ,4) == ['5d', '6d', '7d', '8d']

def test_goDown():
    assert goDown(4 ,4) == ['3d', '2d', '1d']

test_findPossibleMovesKnight()
test_rookMoves()
test_knightMoves()
test_queenMoves()
test_goNorthEast()
test_goSouthEast()
test_goSouthWest()
test_goNorthWest()
test_printMoves()
test_goRight()
test_goleft()
test_goUp()
test_goDown()
