from itertools import count
import numpy as np

def main(debug=False):    
    positions = []
    with open("day8/input.txt") as f:
        positions = np.array([line.strip().split(',') for line in f])
    
    #if debug: print(f"{positions}\n")
    
    circuits = [[i] for i in range(len(positions))]
    if debug: print(f"{circuits}\n")
    
    # Compute distance matrix
    rows, _ = positions.shape
    distanceMatrix = np.zeros((rows, rows), dtype=int)
    for i in range(1,rows):
        for j in range(i):
            distanceMatrix[i][j] = distance(positions[i], positions[j])
            distanceMatrix[j][i] = distanceMatrix[i][j]
    
    mCopy = distanceMatrix.copy()
    
    if debug: print(f"{distanceMatrix}\n")
    
    for _ in range(998):        
        i,j = cooMinMatrix(distanceMatrix)
        if debug : print("Min pos: " + str((i, j)))
        if (i, j) == (-1, -1):
            print("Y a un problème mon gars")
        
        # update circuits
        c2 = circuits.pop(j)
        c1 = circuits.pop(i)
        circuits.append(c1 + c2)
        
        if debug : print("Circuits: " + str(circuits))
        
        # update distance matrix 
        newDistances = []
        for k in range(rows):
            d = min(distanceMatrix[i][k], distanceMatrix[j][k])
            newDistances.append(d)
        
        distanceMatrix = np.append(distanceMatrix, np.array([newDistances]), axis=0)
        newDistances.append(0)
        distanceMatrix = np.append(distanceMatrix, np.array([newDistances]).transpose(), axis=1)
               
        distanceMatrix = np.delete(distanceMatrix, j, axis=0)# 0=row 1=col
        distanceMatrix = np.delete(distanceMatrix, j, axis=1)
        distanceMatrix = np.delete(distanceMatrix, i, axis=0)
        distanceMatrix = np.delete(distanceMatrix, i, axis=1)
        
        rows -= 1
    
    val = cooMinMatrix(distanceMatrix, True)
    print(f"Part 2: {val}")
    
    for i in range(len(mCopy)):
        for j in range(i):
            if mCopy[i][j] == val:
                print(f"Indices: {i}, {j}")
                print(f"Positions: {positions[i]}, {positions[j]}")
                print(f"prod of x axis : {int(positions[i][0]) * int(positions[j][0])} \n")
    
        
    
def cooMinMatrix(matrix,b=False):
    minVal = float('inf')
    minPos = [-1, -1]
    rows, _ = matrix.shape
    for i in range(rows):
        for j in range(i):
            if matrix[i][j] < minVal and matrix[i][j] != 0:
                minVal = matrix[i][j]
                minPos = [i, j]
                
    minPos.sort()
    if b:
        return minVal
    return minPos[0], minPos[1]
    
def distance(pos1, pos2):
    x = (int(pos1[0]) - int(pos2[0]))**2
    y = (int(pos1[1]) - int(pos2[1]))**2
    z = (int(pos1[2]) - int(pos2[2]))**2
    return (x + y + z)**0.5        

if __name__ == '__main__':
    main()