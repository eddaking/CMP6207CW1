import sys
import random
#import matrix in the form a b c;d e f;h i j;.k l m;o p q;r s t;
#where the matrix : [a b c] is the payoff matrix for player 1 and [k l m] is the payoff matrix for the second player
#                  [e f g]                                       [o p q]
#                  [h i j]                                       [r s t]

#2 x 3 matrix : [0 0 0]
#               [0 0 0]

class Matrix:
    def __init__(self, size):
        self.matrix = list()
        for i in range(0,size):
            self.matrix.append(list())
            for j in range(0, size):
                self.matrix[i].append(random.randint(-10,10))
    
    def get(self, i, j):
        return self.matrix[i][j]

    def setElem(self, i, j, val):
        self.matrix[i][j] = val
    
    def print(self):
        for r in self.matrix:
            print(r)

inputMatrix = sys.stdin.read()
flatMatricies = inputMatrix.split(".")
payoffMatrixA = Matrix(5)
payoffMatrixB = Matrix(3)

payoffMatrixA.print()
payoffMatrixB.print()


