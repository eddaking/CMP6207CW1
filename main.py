import sys
import random
# i. Compute all dominant strategy equilibria, if there is any. 
# ii. Compute all pure Nash equilibria, if there is any. 
# iii. Compute at least one mixed Nash equilibrium. 

#2 x 3 matrix : [0 0 0]
#               [0 0 0]

#i = player a strat
#j = player b strat

#this is a class representing a matrix
class Matrix:

    #initalisation method - which takes an input 'size' which generates a random matrix of size x size
    def __init__(self, size):
        self.matrix = list()
        self.size = size
        for i in range(0,size):
            self.matrix.append(list())
            for j in range(0, size):
                self.matrix[i].append(random.randint(-10,10))
    
    #method which returns the specified row
    def getRow(self, i):
        return self.matrix[i]

    #method which generates the a list of the contents of the collumn of the matrix
    def getCol(self, j):
        output = list()
        for row in self.matrix:
            output.append(row[j])
        return output
    
    #getter method for the size of the matrix
    def getSize(self):
        return self.size

    #method which prints the matrix in a moderately human readable form
    def print(self):
        for r in self.matrix:
            print(r)

#method which find dominant strategies in the payoff matricies
def findDominantStrats():
    #find the maxmium and minimum utility for each strategy in payoff matrix for player A
    maxminPayoffsA = list()
    for rowIndex in range(0, payoffMatrixA.getSize()):
        row = payoffMatrixA.getRow(rowIndex)
        vals = [min(row), max(row)]
        maxminPayoffsA.append(vals)

    strictlyDominant = list()
    weaklyDominant = list()
    #now we check each row and see if its minimum utilty is greater than or equal to the maximum of all others
    for testingIndex in range(0,len(vals)):
        dominant = True
        strictly = True
        for rowIndex in range(0,len(maxminPayoffsA)):
            if testingIndex != rowIndex:
                #if the miniumum utility of a row is less than the maximum of another it cannot be dominant and is discarded
                if maxminPayoffsA[testingIndex][0] < maxminPayoffsA[rowIndex][1]:
                    dominant = False
                    break
                #if a row has a min util equal to the max util of another then that row can at best be weakly dominant.
                elif maxminPayoffsA[testingIndex][0] == maxminPayoffsA[rowIndex][1]:
                    strictly = False
        if dominant:
            if strictly:
                strictlyDominant.append(testingIndex)
            else:
                weaklyDominant.append(testingIndex)
    #output the results
    if len(strictlyDominant) == len(weaklyDominant) == 0:
        print("There are no dominant strategies for A")
    elif len(strictlyDominant) > 0:
        print("Player A has a strictly dominant strategy with " + str(strictlyDominant[0]))
    elif len(weaklyDominant) > 0:
        print("Player A has a weakly dominant strategy with " + str(weaklyDominant[0]))

    #find the maxmium and minimum utility for each strategy in payoff matrix for player B
    maxminPayoffsB = list()
    for colIndex in range(0, payoffMatrixB.getSize()):
        col = payoffMatrixB.getCol(colIndex)
        vals = [min(col), max(col)]
        maxminPayoffsB.append(vals)

    strictlyDominant = list()
    weaklyDominant = list()
    #now we check each row and see if its minimum utilty is greater than or equal to the maximum of all others
    for testingIndex in range(0,len(vals)):
        dominant = True
        strictly = True
        for colIndex in range(0,len(maxminPayoffsB)):
            if testingIndex != colIndex:
                #if the miniumum utility of a row is less than the maximum of another it cannot be dominant and is discarded
                if maxminPayoffsB[testingIndex][0] < maxminPayoffsB[colIndex][1]:
                    dominant = False
                    break
                #if a row has a min util equal to the max util of another then that row can at best be weakly dominant.
                elif maxminPayoffsB[testingIndex][0] == maxminPayoffsB[colIndex][1]:
                    strictly = False
        if dominant:
            if strictly:
                strictlyDominant.append(testingIndex)
            else:
                weaklyDominant.append(testingIndex)
                
    #output the results
    if len(strictlyDominant) == len(weaklyDominant) == 0:
        print("There are no dominant strategies for B")
    elif len(strictlyDominant) > 0:
        print("Player B has a strictly dominant strategy with " + str(strictlyDominant[0]))
    elif len(weaklyDominant) > 0:
        print("Player B has a strictly dominant strategy with " + str(weaklyDominant[0]))

#a method which finds pure strategies
def findPureStrats():
    #first we find all the optimal moves for player A given any move by player B and put the pairs of moves into a set
    playerAPotentialPure = set()
    for colIndex in range(0, payoffMatrixA.getSize()):
        col = payoffMatrixA.getCol(colIndex)
        pair = str(col.index(max(col))) + "," + str(colIndex)
        playerAPotentialPure.add(pair)

    #second we find all the optimal moves for player B given any move by player A and put the pairs of moves into a set
    playerBPotentialPure = set()
    for rowIndex in range(0, payoffMatrixB.getSize()):
        row = payoffMatrixB.getRow(rowIndex)
        pair = str(rowIndex) + "," + str(row.index(max(row)))
        playerBPotentialPure.add(pair)

    #third we find the intersection of the two sets i.e the pairs of moves which both players find optimal
    pureStrats = playerAPotentialPure.intersection(playerBPotentialPure)

    #output the pure strategies
    if len(pureStrats) > 0:
        print("Pure strategies: " + str(pureStrats))
    else:
        print("There are no Pure Strategies")

#take a cmd line argument for the size of the matrix
matrixSize = int(sys.argv[1])
#create 2 payoff matricies of size matrix size with values in the range -10 to 10 inclusive
payoffMatrixA = Matrix(matrixSize)
payoffMatrixB = Matrix(matrixSize)


#find dominant strategies
#one strat always yeilds better payoff than any other
findDominantStrats()

#find pure - check each opponent stategy and find best pay off, if both palyers have same optimals then we have pure
findPureStrats()

#find mixed strategy
#create matrix from sim. polynomial eqns from payoff matrix 
#solve with gausian elmination?
#part not attempted

#outputt the Matricies
print("A")
payoffMatrixA.print()
print("B")
payoffMatrixB.print()