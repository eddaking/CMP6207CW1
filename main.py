import sys
#import matrix in the form a b c;d e f;h i j;.k l m;o p q;r s t;
#where the matix : [a b c] is the payoff matrix for player 1 and [k l m] is the payoff matrix for the second player
#                  [e f g]                                       [o p q]
#                  [h i j]                                       [r s t]

#2 x 3 matrix : [0 0 0]
#               [0 0 0]

class Matrix:
    matrix = list()
    def __init__(self, stringInput):
        matix = list()
        tempMatrix = stringInput[0].split(";")
        for r in matrix:
            matrix.append(r.split(" "))
    
    def get(self, i, j):
        return matix[i][j]

    def setElem(self, i, j, val):
        matrix[i][j] = val
    
    def print(self):
        for r in matix:
            print(r)

inputMatrix = sys.stdin.read()
flatMatricies = inputMatrix.split(".")
payoffMatrixA = Matrix(flatMatricies[0])
payoffMatrixB = Matrix(flatMatricies[1])

payoffMatrixA.print()
payoffMatrixB.print()


