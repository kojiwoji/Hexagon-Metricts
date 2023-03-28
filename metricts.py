import math
import hexdirection

class FHexagon:
	### Flat Orientation ###
	def __init__(self, radius, startPos):
		self.radius = radius
		self.outerCircle = radius * 2
		self.innerCircle = math.sqrt(3) * radius
		self.posx, self.posy = startPos
		self.offsetCoordinates = []
		self.cornerPoints = []
		self.hexType = "Flatsided"
		self.direction = {"N": 0, "NE" : 1, "SE" : 2, "S": 3, "SW": 4, "NW": 5}
		self.neighbours = [] # 0 : N, 1 : NE, 2 : SE, 3 : S, 4 : SW, 5 : NW 

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
		hexGridCoordinateList.append(offsetCoordinate)

	def getNeighbor(self, Dint):
		return self.neighbours[self.direction[Dint]]

	def setNeighbor(self, Dint, cellOBJ):
		# Set opposite neighbor and neighbour
		print("Step1")
		#print(cellOBJ)
		#print(Dint)
		# Take in string of the direction and then change it's key
		#self.neighbours.append()
		#cellOBJ.neighbours = cellOBJ.neighbours[cellOBJ.direction[Dint]]
		#Above not working
		print("Step2")
		#cellOBJ.neighbours[cellOBJ.setOppositeNeighbor(Dint)] = self
		print("Working")

	def setOppositeNeighbor(self, Dint):
		if self.direction[Dint] < 3:
			newDirection = self.direction[Dint] + 3
		else:
			newDirection = self.direction[Dint] - 3
		return newDirection

class PHexagon:
	### Pointy Orientation ###
	def __init__(self, radius, startPos):
		self.radius = radius
		self.outerCircle = radius * 2
		self.innerCircle = math.sqrt(3) * radius
		self.posx, self.posy = startPos
		self.offsetCoordinates = []
		self.cornerPoints = []
		self.hexType = "Pointy"

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
		hexGridCoordinateList.append(offsetCoordinate)