import metricts
from copy import copy, deepcopy

class HexGrid:
	def __init__(self, width, height, hexTypeOBJ):
		self.columns = width
		self.rows = height
		self.hexTypeOBJ = hexTypeOBJ
		self.cells = [self.columns * self.rows]
		self.hexCells = []
		self.hexCellsCoordinates = []
		self.hexCellsOffsetCoordinates = []

	def createCell(self, x: int, y: int, i: int, hexTypeOBJ):
		# Check if odd row
		if hexTypeOBJ.hexType == "Flatsided":
			if y % 2 == 0:
				hexTypeOBJ.posx = (x + y * 0.5 - y / 2) * ((hexTypeOBJ.outerCircle * 2)* 1.5)
			else:
				hexTypeOBJ.posx = (x + (y * 0.5 - y / 2) + 0.5) * ((hexTypeOBJ.outerCircle * 2) * 1.5)
			hexTypeOBJ.posy = y * hexTypeOBJ.innerCircle

			hexCopy = copy(hexTypeOBJ)
			hexCopy.updateCorners(hexCopy.posx, hexCopy.posy, self.hexCellsCoordinates)
			hexCopy.assignCoordinates(x, y, self.hexCellsOffsetCoordinates)
			self.hexCells.append(hexCopy)

			# Determine Neighbors
			if(x > 0 and y == 0):
				if ( (x & 1) != 0 ):
					#hexTypeOBJ.setNeighbor(hexTypeOBJ.direction[SW], hexCopy.hexCells[i - 1])
					print("")
				else:
					#hexTypeOBJ.setNeighbor(hexTypeOBJ.direction[NW], hexCopy.hexCells[i - 1])
					print("")
			if (y > 0):
				if ( (x & 1) != 0):
					print("Hex Cells")
					print("Direction")
					print(hexTypeOBJ.direction["SW"])
					print("Object: ")
					print(self.hexCells[i-1])
					print("")
					# int and obj comes into set Neighbour
					hexTypeOBJ.setNeighbor(hexTypeOBJ.direction["SW"], self.hexCells[i - 1])

				else:
					if ( (x & 1) == 0 and x != 0):
						# Set neighbor
						# set Neighbor
						# Set Neigbor
						#print("if ( (x & 1) == 0 and x != 0)")
						#print(x)
						#print(y)
						print("")
					else:
						#print(x)
						#print(y)
						print("")
				#print(x)
				#print(y)
				print("")

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

		else:
			return None

	def createGrid(self):
		### Creating a desired grid ###
		x = 0
		y = 0
		i = 0
		cord = 0
		offsetCord = 0
		## Creating Cells ##
		while y < self.rows:
			y += 1
			while x < self.columns:
				x += 1
				i += 1
				HexGrid.createCell(self, x, y, i, self.hexTypeOBJ)
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
grid01 = HexGrid(2, 2, flatsidedHex)
grid01.createGrid()
### Example 02 ###
pointyHex = metricts.PHexagon(5, (0, 0)) # Radius, Coordinates
grid02 = HexGrid(2, 2, pointyHex)
grid02.createGrid()
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
#for n in grid01.hexCells:
#	print(n.offsetCoordinates)
#	print(n.neighbours)
input("Press any key to continue")