
class ZTetrisPiece():
	iPiece = [
		[True,True,True,True]
	]
	iPiece1 = [
		[True],[True],[True],[True]
	]

	jPiece = [
		[True,False,False],
		[True,True,True]
	]
	jPiece1 = [
		[True,True],
		[True,False],
		[True,False]
	]
	jPiece2 = [
		[True,True,True],
		[False,False,True]
	]
	jPiece3 = [
		[False,True],
		[False,True],
		[True,True]
	]

	lPiece = [
		[False,False,True],
		[True,True,True]
	]
	lPiece1 = [
		[True,False],
		[True,False],
		[True,True]
	]
	lPiece2 = [
		[True,True,True],
		[True,False,False]
	]
	lPiece3 = [
		[True,True],
		[False,True],
		[False,True]
	]

	oPiece = [
		[True,True],
		[True,True]
	]

	sPiece = [
		[False,True,True],
		[True,True,False]
	]
	sPiece1 = [
		[True,False],
		[True,True],
		[False,True]
	]

	tPiece = [
		[False,True,False],
		[True,True,True]
	]
	tPiece1 = [
		[True,False],
		[True,True],
		[True,False]
	]
	tPiece2 = [
		[True,True,True],
		[False,True,False]
	]
	tPiece3 = [
		[False,True],
		[True,True],
		[False,True]
	]

	zPiece = [
		[True,True,False],
		[False,True,True]
	]
	zPiece1 = [
		[False,True],
		[True,True],
		[True,False]
	]

	pieceList = [[iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece],
				 [iPiece1, jPiece1, lPiece1, oPiece, sPiece1, tPiece1, zPiece1],
				 [iPiece, jPiece2, lPiece2, oPiece, sPiece, tPiece2, zPiece],
				 [iPiece1, jPiece3, lPiece3, oPiece, sPiece1, tPiece3, zPiece1]]
	pieceColors = ["red", "yellow", "magenta", "pink", "cyan", "green", "orange"] # store piece colors
	
	def getAllPieces(self):
		return self.pieceList

	def getAllPiecesColors(self):
		return self.pieceColors