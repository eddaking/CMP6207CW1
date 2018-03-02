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
        return matrix[i]

    def getCol(self, j):
        output = list()
        for row in matrix:
            output.append(row[j])
        return output

    def setElem(self, i, j, val):
        self.matrix[i][j] = val
    
    def getSize(self):
        return self.size

    def print(self):
        for r in self.matrix:
            print(r)

matrixSize = sys.stdin.read()
payoffMatrixA = Matrix(matrixSize)
payoffMatrixB = Matrix(matrixSize)

#find dominant strategies
#one strat always yeilds better payoff than any other
minPayoffsA = dict()
for rowIndex in range(0, matrix.getSize()):
    row = matrix.getRow(rowIndex)
    vals = [min(row), max(row)]
    minPayoffsA[rowIndex] = vals

strictlyDominant = list()
weaklyDominant = list()

for testingIndex in range(0,len(vals)):
    dominant = True
    strictly = True
    for rowIndex in range(0,len(vals)):
        if testingIndex != rowIndex:
            if vals[testingIndex][0] < vals[rowIndex][1]:
                dominant = False
                break
            elif vals[testingIndex][0] = vals[rowIndex][1]:
                strictly = False
    if dominant:
        if strictly:
            strictlyDominant.append(testingIndex)
        else:
            weaklyDominant.append(testingIndex)
if len(strictlyDominant) == len(weaklyDominant) == 0:
    print("There are no dominant strategies")
elif len(strictlyDominant) > 0:
    print(len(strictlyDominant))
    print("Player A has a strictly dominant strategy with " + strictlyDominant[0])
elif len(weaklyDominant) > 0:
    print(len(weaklyDominant))
    print("Player A has a strictly dominant strategy with " + weaklyDominant[0])

minPayoffsB = dict()
for rowIndex in range(0, matrix.getSize()):
    row = matrix.getRow(rowIndex)
    vals = [min(row), matrix(row)]
    minPayoffsA[rowIndex] = vals

#find pure - check each opponent stategy and find best pay off, if both palyers have same optimals then we have pure
#player a
for colIndex in range(0, matrix.getSize()):
    col = payoffMatrixA.getCol(colIndex)

    for outcome in col:


#payoffMatrixA.print()
#payoffMatrixB.print()


