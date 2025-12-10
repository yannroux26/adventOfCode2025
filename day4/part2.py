import numpy as np
from tokenize import String

def removeAccessible(matrix, debug=False):
    s = 0
    temp = 1
    while temp != 0:
        temp = 0    
        for i,j in np.ndindex(matrix.shape):
            if matrix[i][j] > 0 and matrix[i][j] < 5:
                temp += 1
                matrix = remove_burden(matrix,i,j)
        s += temp
        if debug: print(f'removed {temp} accessible elements this round')
        
    print(f'\n========== Result: {s} ==========')

def apply_burden(matrix):
    for i,j in np.ndindex(matrix.shape):
        if matrix[i][j] != 0:
            neighbors = getNeighbors(matrix, i, j)
            for r,c in neighbors:
                matrix = apply_burden_el(matrix, r, c, signe=1)
    return matrix

def remove_burden(matrix,i,j):
    neighbors = getNeighbors(matrix, i, j)
    for r,c in neighbors:
        matrix = apply_burden_el(matrix, r, c, signe=-1, min =1)
    matrix[i][j] = 0
    return matrix

def getNeighbors(matrix, row, col):
    len_rows, len_cols = matrix.shape
    neighbors = []
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len_rows and 0 <= c < len_cols:
            neighbors.append((r, c))
    return neighbors

def apply_burden_el(matrix, row,col, signe, min=0):
    if (matrix[row][col] > min):
        matrix[row][col] += signe  
    return matrix

def test():
    return
    
def main(debug=False):
    with open("day4/input.txt") as f:
        matrix_symb = [list(line.strip()) for line in f]
        
    conv = {'.': 0, '@': 1}
    matrix = np.array([[conv[c] for c in row] for row in matrix_symb])
    if debug: print(f'result : {matrix}')
    
    # Apply initial burden
    matrix = apply_burden(matrix)
    if debug: print(f'Matrix after burden application:\n{matrix}')
    
    removeAccessible(matrix, debug=debug)

if __name__ == '__main__':
    #test()
    main()

