import math
from copy import copy, deepcopy

class FHexagon:
	### Flat Orientation ###
	def __init__(self, radius, startPos):
		self.radius = radius
		self.outerCircle = radius * 2
		self.innerCircle = math.sqrt(3) * radius
		self.posx, self.posy = startPos
		self.offsetCoordinates = []
		self.cubeCoordinates = []
		self.cornerPoints = []
		self.hexType = "Flatsided"
		self.direction = {"N": 0, "NE" : 1, "SE" : 2, "S": 3, "SW": 4, "NW": 5}
		self.placeHolder = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None} # 0 : obj, 1 : obj, 2 : obj, 3 : obj, 4 : obj, 5 : obj 
		self.neighbours = self.placeHolder.copy()
		self.distance = 0
		
	def getCorners(self):
		### Postion for corners ###
		self.cornerPoints.append((0.5 * self.outerCircle, self.innerCircle))
		self.cornerPoints.append((self.outerCircle, 0))
		self.cornerPoints.append((0.5 * self.outerCircle, -abs(self.innerCircle)))
		self.cornerPoints.append((-0.5 * self.outerCircle, -abs(self.innerCircle)))
		self.cornerPoints.append((-abs(self.outerCircle), 0))
		self.cornerPoints.append((-0.5 * self.outerCircle, self.innerCircle))

	def updateCorners(self, x, y, cornerList):
		### Update already existing corners ###
		## Used when inserting hexagons inside a grid ##
		newCorners = []
		newCorners.append((0.5 * self.outerCircle + x, self.innerCircle + y))
		newCorners.append((self.outerCircle + x, 0 + y))
		newCorners.append((0.5 * self.outerCircle + x, -abs(self.innerCircle) + y))
		newCorners.append((-0.5 * self.outerCircle + x, -abs(self.innerCircle) + y))
		newCorners.append((-abs(self.outerCircle) + x, 0 + y))
		newCorners.append((-0.5 * self.outerCircle + x, self.innerCircle + y))
		cornerList.append(newCorners)

	def assignCoordinates(self, x, y, hexGridCoordinateList):
		### Assigning coordinate for mentioned hexagon ###
		offsetCoordinate = (x, y)
		self.offsetCoordinates = (x, y)
		hexGridCoordinateList.append(offsetCoordinate)

	def getNeighbor(self, Dint):
		if self.neighbours[Dint] == None:
			return None
		else:
			returnNeigh = self.neighbours[Dint]
			return returnNeigh

	def setNeighbor(self, Dint, cellOBJ, boolean):
		if boolean != None:
			self.placeHolder[Dint] = cellOBJ
			opposite = cellOBJ.setOppositeNeighbor(Dint)
			cellOBJ.placeHolder = cellOBJ.neighbours.copy()
			cellOBJ.placeHolder[opposite] = self
			cellOBJ.neighbours = cellOBJ.placeHolder.copy()
			self.neighbours = self.placeHolder.copy()
		else:
			self.placeHolder[Dint] = None
			cellOBJ.placeHolder = cellOBJ.neighbours.copy()
			cellOBJ.neighbours = cellOBJ.placeHolder.copy()

	def setOppositeNeighbor(self, Dint):
		if Dint < 3:
			newDirection = Dint + 3
		else:
			newDirection = Dint - 3
		return newDirection

	def distanceTo(self, offsetCoordinates):
		x1,y1 = self.offsetCoordinates
		x2, y2 = offsetCoordinates
		return (abs(x1 - x2) + abs(y1 - y2))

class PHexagon:
	### Pointy Orientation ###
	def __init__(self, radius, startPos):
		self.radius = radius
		self.outerCircle = radius * 2
		self.innerCircle = math.sqrt(3) * radius
		self.posx, self.posy = startPos
		self.offsetCoordinates = []
		self.cubeCoordinates = []
		self.cornerPoints = []
		self.hexType = "Pointy"
		self.direction = {"NE": 0, "E" : 1, "SE" : 2, "SW": 3, "W": 4, "NW": 5}
		self.placeHolder = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None} # 0 : obj, 1 : obj, 2 : obj, 3 : obj, 4 : obj, 5 : obj 
		self.neighbours = self.placeHolder.copy()
		self.distance = 0

	def getCorners(self):
	        ### Postion for corners ###
	        self.cornerPoints.append((0, self.outerCircle))
	        self.cornerPoints.append((self.innerCircle, 0.5 * self.outerCircle))
	        self.cornerPoints.append((self.innerCircle, -0.5 * self.outerCircle))
	        self.cornerPoints.append((0, -abs(self.outerCircle)))
	        self.cornerPoints.append((-abs(self.innerCircle), -0.5 * self.outerCircle))
	        self.cornerPoints.append((-abs(self.innerCircle), 0.5 * self.outerCircle))

	def updateCorners(self, x, y, cornerList):
		### Update already existing corners ###
		## Used when inserting hexagons inside a grid ##
		newCorners = []
		newCorners.append((0 + x, self.outerCircle + y))
		newCorners.append((self.innerCircle + x, 0.5 * self.outerCircle + y))
		newCorners.append((self.innerCircle + x, -0.5 * self.outerCircle + y))
		newCorners.append((0 + x, -abs(self.outerCircle) + y))
		newCorners.append((-abs(self.innerCircle) + x, -0.5 * self.outerCircle + y))
		newCorners.append((-abs(self.innerCircle) + x, 0.5 * self.outerCircle + y))
		cornerList.append(newCorners)

	def assignCoordinates(self, x, y, hexGridCoordinateList):
		### Assigning coordinate for mentioned hexagon ###
		offsetCoordinate = (x, y)
		self.offsetCoordinates = (x, y)
		hexGridCoordinateList.append(offsetCoordinate)

	def getNeighbor(self, Dint):
		if self.neighbours[Dint] == None:
			return None
		else:
			returnNeigh = self.neighbours[Dint]
			return returnNeigh

	def setNeighbor(self, Dint, cellOBJ, boolean):
		if boolean != None:
			self.placeHolder[Dint] = cellOBJ
			opposite = cellOBJ.setOppositeNeighbor(Dint)
			cellOBJ.placeHolder = cellOBJ.neighbours.copy()
			cellOBJ.placeHolder[opposite] = self
			cellOBJ.neighbours = cellOBJ.placeHolder.copy()
			self.neighbours = self.placeHolder.copy()
		else:
			self.placeHolder[Dint] = None
			cellOBJ.placeHolder = cellOBJ.neighbours.copy()
			cellOBJ.neighbours = cellOBJ.placeHolder.copy()

	def setOppositeNeighbor(self, Dint):
		if Dint < 3:
			newDirection = Dint + 3
		else:
			newDirection = Dint - 3
		return newDirection

	def distanceTo(self, offsetCoordinates):
		x1,y1 = self.offsetCoordinates
		x2, y2 = offsetCoordinates
		return (abs(x1 - x2) + abs(y1 - y2))