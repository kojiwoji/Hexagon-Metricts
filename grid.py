import metricts
from copy import copy, deepcopy

class HexGrid:
	def __init__(self, width, height, hexTypeOBJ):
		self.maxValue = 2147483647
		self.columns = width
		self.rows = height
		self.hexTypeOBJ = hexTypeOBJ
		self.cells = [self.columns * self.rows]
		self.hexCells = []
		self.hexCellsCoordinates = []
		self.hexCellsOffsetCoordinates = []

	def searchCell(self, cell):
		qurt = 0
		while qurt < len(self.hexCells):
			self.hexCells[qurt].distance = self.maxValue
			qurt += 1
		queue = []
		cell.distance = 0
		queue.append(cell)
		while len(queue) > 0:
			current = queue[0]
			d = 0
			while d <= 5:
				neighbor = current.getNeighbor(d)
				if neighbor != None:
					None
				if (neighbor != None and neighbor.distance == self.maxValue):
					neighbor.distance = current.distance + 1
					queue.append(neighbor)
				d += 1
			queue.pop(0)

	def findDistanceTo(self, selectedCell):
		HexGrid.searchCell(self, selectedCell)

	def createCell(self, x: int, y: int, i: int, hexTypeOBJ):
		# Check if odd row
		if hexTypeOBJ.hexType == "Flatsided":
			if x > 0:
				if x % 2 == 0:
					hexTypeOBJ.posx = ((x + ((y * 0.5 - y / 2))) * ((hexTypeOBJ.outerCircle * 2)) * 0.75)
					hexTypeOBJ.posy = (y * 2) * hexTypeOBJ.innerCircle
				else:
					hexTypeOBJ.posx = ((x + ((y * 0.5 - y / 2))) * ((hexTypeOBJ.outerCircle * 2)) * 0.75)
					hexTypeOBJ.posy = (y * 2 + 1) * hexTypeOBJ.innerCircle
			
			else:
				hexTypeOBJ.posx = (x + y * 0.5 - y / 2) * ((hexTypeOBJ.outerCircle * 2))
				hexTypeOBJ.posy = (y * 2) * hexTypeOBJ.innerCircle
			
			hexCopy = copy(hexTypeOBJ)
			hexCopy.updateCorners(hexCopy.posx, hexCopy.posy, self.hexCellsCoordinates)
			hexCopy.assignCoordinates(x, y, self.hexCellsOffsetCoordinates)
			self.hexCells.append(hexCopy)
			# Determine Neighbors
			if (x > 0 and y == 0): # 1st row is a special snowflake
				if ((x & 1) != 0):
					hexCopy.setNeighbor(hexCopy.direction["SW"], self.hexCells[i - 1], True)
				else:
					hexCopy.setNeighbor(hexCopy.direction["NW"], self.hexCells[i - 1], True)
			if (y > 0):
				if ((x & 1) != 0):
					if x != 0 and x != self.columns - 1:
						hexCopy.setNeighbor(hexCopy.direction["SW"], self.hexCells[i - 1], True)
					
					elif x == self.columns - 1:
						hexCopy.setNeighbor(hexCopy.direction["SE"], self.hexCells[i - self.columns - 1], None)
						hexCopy.setNeighbor(hexCopy.direction["SW"], self.hexCells[i - 1], True)			
				else:
					if x != 0 and x != self.columns - 1:
						hexCopy.setNeighbor(hexCopy.direction["NW"], self.hexCells[i - 1], True)
						hexCopy.setNeighbor(hexCopy.direction["SE"], self.hexCells[i - self.columns + 1], True)
						hexCopy.setNeighbor(hexCopy.direction["SW"], self.hexCells[i - self.columns - 1], True)

					elif x == self.columns - 1:
						hexCopy.setNeighbor(hexCopy.direction["NW"], self.hexCells[i - 1], True)
						hexCopy.setNeighbor(hexCopy.direction["SE"], self.hexCells[i - self.columns + 1], None)
						hexCopy.setNeighbor(hexCopy.direction["SW"], self.hexCells[i - self.columns - 1], True)

					else:
						hexCopy.setNeighbor(hexCopy.direction["SW"], self.hexCells[i - self.columns - 1], None)
						hexCopy.setNeighbor(hexCopy.direction["NW"], self.hexCells[i - 1], None)
						hexCopy.setNeighbor(hexCopy.direction["SE"], self.hexCells[i - self.columns + 1], True)

				hexCopy.setNeighbor(hexCopy.direction["S"], self.hexCells[i - self.columns], True)


		elif hexTypeOBJ.hexType == "Pointy":
			if y % 2 == 0:
				hexTypeOBJ.posx = (x + (y * 0.5 - y / 2) + 0.5) * (hexTypeOBJ.innerCircle * 2)
			else:
				hexTypeOBJ.posx = (x + y * 0.5 - y / 2) * (hexTypeOBJ.innerCircle * 2)
			hexTypeOBJ.posy = y * (hexTypeOBJ.outerCircle * 1.5)
			hexCopy = copy(hexTypeOBJ)
			hexCopy.updateCorners(hexCopy.posx, hexCopy.posy, self.hexCellsCoordinates)
			hexCopy.assignCoordinates(x, y, self.hexCellsOffsetCoordinates)
			self.hexCells.append(hexCopy)

			# Determine Neighbors
			if x > 0:
				hexCopy.setNeighbor(hexCopy.direction["W"], self.hexCells[i - 1], True)
			else:
				hexCopy.setNeighbor(hexCopy.direction["W"], self.hexCells[i - 1], None)
			if y > 0:
				if ((y & 1) == 0):
					hexCopy.setNeighbor(hexCopy.direction["SE"], self.hexCells[i - self.columns], True)
					if (x > 0):
						hexCopy.setNeighbor(hexCopy.direction["SW"], self.hexCells[i - self.columns - 1], True)
				else:
					if x != self.columns - 1:
						hexCopy.setNeighbor(hexCopy.direction["SW"], self.hexCells[i - self.columns], True)
						hexCopy.setNeighbor(hexCopy.direction["SE"], self.hexCells[i - self.columns + 1], True)
					else:
						hexCopy.setNeighbor(hexCopy.direction["SE"], self.hexCells[i - self.columns + 1], None)
						hexCopy.setNeighbor(hexCopy.direction["SW"], self.hexCells[i - self.columns], True)
	def createGrid(self):
		### Creating a desired grid ###
		x = 0
		y = 0
		i = 0
		cord = 0
		offsetCord = 0
		## Creating Cells ##
		while y < self.rows:
			while x < self.columns:
				HexGrid.createCell(self, x, y, i, self.hexTypeOBJ)
				x += 1
				i += 1
			y += 1
			x = 0

		## Assign new coodinates to corresponding object ##
		for obj in self.hexCells:
			if  cord < len(self.hexCellsCoordinates):
				obj.cornerPoints = self.hexCellsCoordinates[cord]
			cord += 1
			if offsetCord < i:
				obj.offsetCoordinates = self.hexCellsOffsetCoordinates[offsetCord]
			offsetCord += 1

### Example 01 ###
flatsidedHex = metricts.FHexagon(5, (0, 0)) # Radius, Coordinates
grid01 = HexGrid(8, 8, flatsidedHex)
grid01.createGrid()
### Example 02 ###
#pointyHex = metricts.PHexagon(5, (0, 0)) # Radius, Coordinates
#grid02 = HexGrid(8, 8, pointyHex)
#grid02.createGrid()
'''
print("### Example 01 ###")
for n in grid01.hexCells:
	print("It's the following Hex Type: " + n.hexType)
	print("It has the following coordinates: " + str((n.posx, n.posy)))
	print("It has these offset Coordinates: " + str(n.offsetCoordinates))
	print("It has these corners: " + str(n.cornerPoints))
	print("")
print("")
print("### Example 02 ###")
for n in grid02.hexCells:
	print("It's the following Hex Type: " + n.hexType)
	print("It has the following coordinates: " + str((n.posx, n.posy)))
	print("It has these offset Coordinates: " + str(n.offsetCoordinates))
	print("It has these corners: " + str(n.cornerPoints))
	print("")
'''

ab = 0
currentDir = ""
'''
print("-------------------------")
for n in grid01.hexCells:
	abr = 0
	print("")
	print("-------------------------")
	print("Test: " + str(n.offsetCoordinates))
	print("-------------------------")
	for q in n.neighbours:
		if abr == 0:
			currentDir = "N"
		elif abr == 1:
			currentDir = "NE"
		elif abr == 2:
			currentDir = "SE"
		elif abr == 3:
			currentDir = "S"
		elif abr == 4:
			currentDir = "SW"
		elif abr == 5:
			currentDir = "NW"
		qui = n.neighbours[abr]
		if qui == None:
			print(currentDir + ": " + str(qui))
		else:
			print(currentDir + ": " + str(qui.offsetCoordinates))
		abr += 1
print("-------------------------")
'''
'''
print("-------------------------")
for n in grid02.hexCells:
	abr = 0
	print("")
	print("-------------------------")
	print("Test: " + str(n.offsetCoordinates))
	print("-------------------------")
	for q in n.neighbours:
		if abr == 0:
			currentDir = "NE"
		elif abr == 1:
			currentDir = "E"
		elif abr == 2:
			currentDir = "SE"
		elif abr == 3:
			currentDir = "SW"
		elif abr == 4:
			currentDir = "W"
		elif abr == 5:
			currentDir = "NW"
		qui = n.neighbours[abr]
		if qui == None:
			print(currentDir + ": " + str(qui))
		else:
			print(currentDir + ": " + str(qui.offsetCoordinates))
		abr += 1
'''

boll = grid01.hexCells[0]
grid01.findDistanceTo(boll)

print("-------------------------")
print("Selected cell: " + str(boll.offsetCoordinates))
print("")
for n in grid01.hexCells:
	qr = n.distance
	print(n.offsetCoordinates)
	print("Distance: " + str(qr))
	print("")


print("-------------------------")
input("Press any key to continue")