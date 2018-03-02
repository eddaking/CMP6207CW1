import sys
import random
# i. Compute all dominant strategy equilibria, if there is any. 
# ii. Compute all pure Nash equilibria, if there is any. 
# iii. Compute at least one mixed Nash equilibrium. 

#2 x 3 matrix : [0 0 0]
#               [0 0 0]

#i = player a strat
#j = player b strat
class Matrix:
    def __init__(self, size):
        self.matrix = list()
        self.size = size
        for i in range(0,size):
            self.matrix.append(list())
            for j in range(0, size):
                self.matrix[i].append(random.randint(-10,10))
    
    def get(self, i, j):
        return self.matrix[i][j]

    def getRow(self, i):
        return self.matrix[i]

    def getCol(self, j):
        output = list()
        for row in self.matrix:
            output.append(row[j])
        return output

    def setElem(self, i, j, val):
        self.matrix[i][j] = val
    
    def getSize(self):
        return self.size

    def print(self):
        for r in self.matrix:
            print(r)

def findDominantStrats():
    minPayoffsA = list()
    for rowIndex in range(0, payoffMatrixA.getSize()):
        row = payoffMatrixA.getRow(rowIndex)
        vals = [min(row), max(row)]
        minPayoffsA.append(vals)

    strictlyDominant = list()
    weaklyDominant = list()

    for testingIndex in range(0,len(vals)):
        dominant = True
        strictly = True
        for rowIndex in range(0,len(minPayoffsA)):
            if testingIndex != rowIndex:
                if minPayoffsA[testingIndex][0] < minPayoffsA[rowIndex][1]:
                    dominant = False
                    break
                elif minPayoffsA[testingIndex][0] == minPayoffsA[rowIndex][1]:
                    strictly = False
        if dominant:
            if strictly:
                strictlyDominant.append(testingIndex)
            else:
                weaklyDominant.append(testingIndex)
    if len(strictlyDominant) == len(weaklyDominant) == 0:
        print("There are no dominant strategies")
    elif len(strictlyDominant) > 0:
        print("Player A has a strictly dominant strategy with " + str(strictlyDominant[0]))
    elif len(weaklyDominant) > 0:
        print("Player A has a strictly dominant strategy with " + str(weaklyDominant[0]))

    minPayoffsA = list()
    for colIndex in range(0, payoffMatrixB.getSize()):
        col = payoffMatrixB.getCol(colIndex)
        vals = [min(col), max(col)]
        minPayoffsA.append(vals)

    strictlyDominant = list()
    weaklyDominant = list()

    for testingIndex in range(0,len(vals)):
        dominant = True
        strictly = True
        for colIndex in range(0,len(minPayoffsA)):
            if testingIndex != colIndex:
                if minPayoffsA[testingIndex][0] < minPayoffsA[colIndex][1]:
                    dominant = False
                    break
                elif minPayoffsA[testingIndex][0] == minPayoffsA[colIndex][1]:
                    strictly = False
        if dominant:
            if strictly:
                strictlyDominant.append(testingIndex)
            else:
                weaklyDominant.append(testingIndex)
    if len(strictlyDominant) == len(weaklyDominant) == 0:
        print("There are no dominant strategies")
    elif len(strictlyDominant) > 0:
        print("Player B has a strictly dominant strategy with " + str(strictlyDominant[0]))
    elif len(weaklyDominant) > 0:
        print("Player B has a strictly dominant strategy with " + str(weaklyDominant[0]))



matrixSize = int(sys.argv[1])
payoffMatrixA = Matrix(matrixSize)
payoffMatrixB = Matrix(matrixSize)


#find dominant strategies
#one strat always yeilds better payoff than any other
findDominantStrats()

#find pure - check each opponent stategy and find best pay off, if both palyers have same optimals then we have pure
#player a
playerAPotentialPure = set()
for colIndex in range(0, payoffMatrixA.getSize()):
    col = payoffMatrixA.getCol(colIndex)
    pair = [col.index(max(col)), colIndex]
    playerAPotentialPure.add(pair)

playerAPotentialPure = list()
for rowIndex in range(0, payoffMatrixB.getSize())
    row = payoffMatrixB.getRow(rowIndex)
    pair = [rowIndex, row.index(max(row))]
    playerBPotentialPure.add(pair)

pureStrats = playerAPotentialPure.intersection(playerBPotentialPure)
print(pureStrats)

print("A")
payoffMatrixA.print()
print("B")
payoffMatrixB.print()