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

#player a
for row in matrix.getRow

payoffMatrixA.print()
payoffMatrixB.print()


