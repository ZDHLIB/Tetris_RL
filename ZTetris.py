from Tkinter import *
from ZTetrisPiece import *
import random



def drawCell(row, col, color):
	board = canvas.board
	topX = canvas.cellSize*(1+col)
	topY = canvas.cellSize*(1+row)
	bottomX = topX + canvas.cellSize
	bottomY = topY + canvas.cellSize
	thickness = (canvas.cellSize*0.02)
	canvas.create_rectangle(topX,topY,bottomX,bottomY,fill="black")
	canvas.create_rectangle(topX+thickness,topY+thickness,\
							bottomX-thickness,bottomY-thickness,fill=color)


def drawScore():
	output = "Score: " + str(canvas.score) # display score
	canvas.create_text(240, 25, text=output, fill="black", font="Ariel") 
	if canvas.isGameOver:
		print canvas.cols, canvas.rows
		canvas.create_text(canvas.cellSize*(canvas.cols+2)/2, 
			               canvas.cellSize*(canvas.rows+2)-20, 
			               text="Game Over!", fill="red", font=("Helvetica", "32"))


def redrawBoard():
	canvas.delete(ALL)
	canvas.create_rectangle(0, 0, canvas.cellSize*(2+canvas.cols), 
		                    canvas.cellSize*(2+canvas.rows), fill="orange")
	initGameBoard()		                   	


def removeRows():
	board = canvas.board
	removeList = []
	for r in range(canvas.rows-1, -1, -1):
		if canvas.emptyColor not in canvas.board[r]:
			removeList.append(r)

	for r in removeList:
		print 'pop:', r
		canvas.board.pop(r)

	for r in removeList:
		canvas.board.insert(0, [canvas.emptyColor]*canvas.cols)

	canvas.score += len(removeList)
	# print board, removeList
	redrawBoard()


def updataBoard():
	rowOffset = 0
	for pieceRow in canvas.fallingPiece:
		colOffset = 0
		for cell in pieceRow:
			if cell == True:
				newRow = canvas.fallingPieceRow + rowOffset
				newCol = canvas.fallingPieceCol + colOffset
				canvas.board[newRow][newCol] = canvas.fallingPieceColor
			colOffset += 1
		rowOffset += 1
	removeRows()


def drawFallingPiece():
	redrawBoard()
	rowOffset = 0
	for pieceRow in canvas.fallingPiece:
		colOffset = 0
		for cell in pieceRow:
			if cell == True:
				row = canvas.fallingPieceRow + rowOffset
				col = canvas.fallingPieceCol + colOffset
				if not canvas.isGameOver:
					drawCell(row, col, canvas.fallingPieceColor)
			colOffset += 1
		rowOffset += 1


def isMovingLegal(piece, currRow, currCol):
	rowOffset = 0
	for pieceRow in piece:
		colOffset = 0
		for cell in pieceRow:
			if cell == True:
				newRow = currRow + rowOffset
				newCol = currCol + colOffset
				if newCol >= canvas.cols or newCol < 0 or \
				   newRow >= canvas.rows or canvas.board[newRow][newCol] != canvas.emptyColor:
					return False
			colOffset += 1
		rowOffset += 1
	return True


def rotateFallingPiece():
	zPiecesStatus = canvas.zPiecesStatus
	zPiecesList = canvas.zPiecesList[zPiecesStatus]
	zPiecesIndex = zPiecesList.index(canvas.fallingPiece)
	zPiecesStatus = (zPiecesStatus + 1) % 4
	fallingPiece = canvas.zPiecesList[ zPiecesStatus ][ zPiecesIndex ]
	if isMovingLegal(fallingPiece, canvas.fallingPieceRow, canvas.fallingPieceCol):
		canvas.fallingPiece = fallingPiece
		canvas.fallingPieceWidth = len(canvas.fallingPiece[0])
		canvas.fallingPieceHeight = len(canvas.fallingPiece)
		canvas.zPiecesStatus = zPiecesStatus
	drawFallingPiece()


def moveFallingPiece(rowOffset, colOffset):
	redrawBoard()
	canvas.fallingPieceRow += rowOffset
	canvas.fallingPieceCol += colOffset
	if not isMovingLegal(canvas.fallingPiece, 
		                 canvas.fallingPieceRow,
		                 canvas.fallingPieceCol):
		canvas.fallingPieceRow -= rowOffset
		canvas.fallingPieceCol -= colOffset	
		drawFallingPiece()
		return False
	drawFallingPiece()
	return True


def newPiece():
	for item in canvas.board[0]:
		if item != canvas.emptyColor:
			canvas.isGameOver = True
			return

	zPiecesList = canvas.zPiecesList[canvas.zPiecesStatus]
	zPiecesColors = canvas.zPiecesColors
	canvas.fallingPiece = zPiecesList[random.randint(0,len(zPiecesList)-1)]
	canvas.fallingPieceColor = zPiecesColors[zPiecesList.index(canvas.fallingPiece)]
	canvas.fallingPieceRow = 0
	canvas.fallingPieceCol = canvas.cols / 2 - (len(canvas.fallingPiece[0]) / 2)
	canvas.fallingPieceWidth = len(canvas.fallingPiece[0])
	canvas.fallingPieceHeight = len(canvas.fallingPiece)
	drawFallingPiece()


def initGameBoard():
	drawScore()
	board = canvas.board
	for r in range(canvas.rows):
		for c in range(canvas.cols):
			drawCell(r, c, board[r][c])


def run(speed=500):
	redrawBoard()
	if canvas.isGameOver:
		return
	canvas.after(speed, run, 500)
	if not moveFallingPiece(rowOffset=1,colOffset=0):
		updataBoard()
		newPiece()


def initPieces(**kwargs):
	zPieces = ZTetrisPiece()
	zPiecesList = zPieces.getAllPieces()
	zPiecesColors = zPieces.getAllPiecesColors()
	canvas.zPiecesList = zPiecesList
	canvas.zPiecesColors = zPiecesColors
	canvas.zPiecesStatus = 0


def initCanvas(**kwargs):
	root = kwargs.get('root')
	cellSize = kwargs.get('cellSize', 40)
	cols = kwargs.get('cols',10)
	rows = kwargs.get('rows', 10)
	emptyColor = kwargs.get('emptyColor', 'blue')
	isGameOver = kwargs.get('isGameOver', False)

	global canvas
	canvas = Canvas(root, width=cellSize * (cols+2), height=cellSize*(rows+2))
	canvas.pack()
	canvas.cellSize = cellSize
	canvas.score = 0
	canvas.emptyColor = 'blue'
	canvas.board = [ [emptyColor] * cols for row in range(rows) ]
	canvas.cols = cols
	canvas.rows = rows
	canvas.isGameOver = False

	canvas.create_rectangle(0, 0, cellSize*(2+cols), cellSize*(2+rows), fill="orange")


def keyPressed(event):
	if event.keysym == "Down":
		if not moveFallingPiece(rowOffset=1,colOffset=0):
			updataBoard()
	elif event.keysym == "Right":
		moveFallingPiece(rowOffset=0,colOffset=1)
	elif event.keysym == "Left":
		moveFallingPiece(rowOffset=0,colOffset=-1)
	elif event.keysym == "Up":
		rotateFallingPiece()
		moveFallingPiece(rowOffset=0,colOffset=0)


def start(rows=15,cols=10,cellSize=40):
	root = Tk()
	root.resizable(width=0, height=0)
	initCanvas(root=root,cellSize=cellSize,cols=cols,rows=rows,emptyColor='blue',isGameOver=False)
	initPieces()
	initGameBoard()
	newPiece()
	run()
	root.bind("<Key>", keyPressed)
	root.mainloop()


if __name__ == '__main__':
	start(rows=15,cols=10,cellSize=40)