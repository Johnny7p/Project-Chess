# Pieces
from Chess import *
class Position(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y


class Pieces(object): 
	def __init__(self,position,color):
		self.Pos = position
		self.color = color
		
	def __repr__(self):
		return self.type
		

	def move(self,Pos2):
		self.Pos = Pos2

class Pawn(Pieces):
	def __init__(self,position,color):
		self.hasMoved = False
		self.type = "P"
		super().__init__(position,color)
	
	def move(self,Pos2):
		if not self.hasMoved:
			if Pos2.y - self.Pos.y <= 2 and Pos2.x == self.Pos.x:
				self.Pos = Pos2
		else:
			if Pos2.y - self.Pos.y <= 2 and Pos2.x == self.Pos.x:
				return True
		self.hasMoved = True

class Rook(Pieces):
	type = "R"
	def move(self,Pos2):
		if (Pos2.x != Pos.x and Pos2.y == Pos2.x) or (Pos2.x == Pos.x and Pos2.y != Pos2.x):
			self.Pos = Pos2

class Knight(Pieces):
	type = "N"
	def move(self,Pos2):
		#make it move in an L.
		self.Pos == Pos2

class Bishop(Pieces):
	type = "B"
	def move(self,Pos2):
		if abs(self.Pos.x - Pos.x) == abs(self.Pos.y - Pos2.y):
			self.Pos == Pos2

class Queen(Pieces):
	type = "B"
	def move(self,Pos2):
		# Make Queen Move in All directions
		self.Pos == Pos2

class King(Pieces):
	type = "K"
	def move(self,Pos2):
		#Make King move 1 space in All Directions
		self.Pos == Pos2
















		

