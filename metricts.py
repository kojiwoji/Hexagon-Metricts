import math

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