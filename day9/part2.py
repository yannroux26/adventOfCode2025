import numpy as np

def main(debug=False):
    positions = []
    with open("day9/input.txt") as f:
        positions = np.array([line.strip().split(',') for line in f])
    
    # proportionality lists
    listLenX = list(dict.fromkeys(int(pos[0]) for pos in positions)) #remove duplicates
    listLenX.sort()
    listLenY = list(dict.fromkeys(int(pos[1]) for pos in positions)) #remove duplicates
    listLenY.sort()
    
    lx = len(listLenX)
    ly = len(listLenY)
    if debug: print(f"len listLenX : {len(listLenX)}, len listLenY : {len(listLenY)}")
    
    matRedPos = np.zeros((lx,ly), dtype=int) # matrix
    redPositions = [] # list
    for pos in positions:
        x = int(pos[0])
        y = int(pos[1])
        i = listLenX.index(x)
        j = listLenY.index(y)
        matRedPos[i][j] = 1
        redPositions.append((i,j))
    
    if debug: print(f"matRedPos :\n{matRedPos.transpose()}")
    else: print("Reduced Matrice of position done")
    
    reducedMatrice = np.zeros((lx, ly), dtype=int)
    prev = 0
    for j in range(ly):
        if matRedPos[0][j] == 1:
            prev = 1-prev
        reducedMatrice[0][j] = prev
    for i in range(1, lx):
        prev = reducedMatrice[i-1][0]
        if matRedPos[i][0] == 1:
            prev = 1-prev
        reducedMatrice[i][0] = prev
            
        for j in range(1, ly):
            if np.sum(matRedPos[i+1:,j]) % 2 == 1: # we cross a edge
                prev = 1-prev
            reducedMatrice[i][j] = prev

    if debug: print(f"Reduced filled matrice :\n{reducedMatrice.transpose()}")
    else: print("Reduced filled Matrice done")

    # Final area calculation
    max_area = 0
    for i in range(len(redPositions)):
        for j in range(i, len(redPositions)):
            area = rectArea(redPositions[i], redPositions[j],listLenX, listLenY)
            if isAvailable(redPositions[i], redPositions[j], reducedMatrice):
                if area > max_area:
                    max_area = area
                    if debug: print(f"Bigger area found : {max_area}")
    print(f"Max area found : {max_area}")

def isAvailable(pos1, pos2, matrix):
    x1 = min(int(pos1[0]), int(pos2[0]))
    x2 = max(int(pos1[0]), int(pos2[0]))
    y1 = min(int(pos1[1]), int(pos2[1]))
    y2 = max(int(pos1[1]), int(pos2[1]))
    subMatrix = matrix[x1:x2, y1:y2]
    if np.any(subMatrix == 0):
        return False
    return True

def rectArea(pos1, pos2, listLenX, listLenY):
    x = abs(int(listLenX[pos1[0]]) - int(listLenX[pos2[0]]))+1
    y = abs(int(listLenY[pos1[1]]) - int(listLenY[pos2[1]]))+1
    return x * y
    
if __name__ == '__main__':
    main()