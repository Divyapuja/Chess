In python, and given standard algebraic notation of a chess board (see below), write code that will:

Accept two parameters:
1.	Type of chess piece (Queen, Rook, Knight)
2.	Current position on a chess board (for example: d2)

Return:
	A list of all the potential board positions the given piece could advance to, with one move, from the given position, with the assumption there are no other pieces on the board.

# Rules:
- You do not have to implement the solution for every piece type, but the solution must implement at least the following: Queen, Rook and Knight.
- You may not use any external/non-core libraries: use only primitives and built-ins.
- Please provide test coverage for your work.

# Example:
`$ chessercise.py --piece KNIGHT --position d2`

The response should be:  `“b1, f1, b3, f3,c4, e4"`

# Algebraic Notation Legend: 
<img src="https://github.com/Divyapuja/Chess/blob/master/AlgebricNotation.png" alt="Algebric notation" width="250" height="250">

# Example
- python chessercise.py --piece KNIGHT --position d2

	```b1,f1,b3,f3,c4,e4```

- python chessercise.py --piece QUEEN --position d2

	```c1,d1,e1,a2,b2,c2,e2,f2,g2,h2,c3,d3,e3,b4,d4,f4,a5,d5,g5,d6,h6,d7,d8```

- python chessercise.py --piece ROOK --position d2

	```d1,a2,b2,c2,e2,f2,g2,h2,d3,d4,d5,d6,d7,d8```

- python chessercise.py --piece KNIGHT --position p2
	```
	Traceback (most recent call last):
	  File "chessercise.py", line 198, in <module>
	    main()
	  File "chessercise.py", line 183, in main
	    raise ValueError('Invalid location')
	ValueError: Invalid location
	```

- python chessercise.py --piece KNIGHT --position d9
	```
	Traceback (most recent call last):
	  File "chessercise.py", line 198, in <module>
	    main()
	  File "chessercise.py", line 174, in main
	    raise ValueError('Invalid location')
	ValueError: Invalid location
	```

- python chessercise.py --piece KING --position d2
	```
	Traceback (most recent call last):
	  File "chessercise.py", line 198, in <module>
	    main()
	  File "chessercise.py", line 170, in main
	    raise ValueError('Invalid piece')
	ValueError: Invalid piece
	```
# Coverage
- Execute below commands -
```
pip install coverage
coverage run test_chessercise.py --piece KNIGHT --position d2
coverage run test_chessercise.py --piece ROOK --position d2
coverage run test_chessercise.py --piece QUEEN --position d2
coverage html
```
<img src="https://github.com/Divyapuja/Chess/blob/master/CoverageReport.png" alt="Coverage Report" width="400" height="250">
