import numpy as np
from tokenize import String

def countAccessible(matrix, debug=False):
    s = 0
    matrix = apply_burden(matrix)
    if debug: print(f'Matrix after burden application:\n{matrix}')
    for i,j in np.ndindex(matrix.shape):
        if matrix[i][j] > 0 and matrix[i][j] < 5:
            s += 1
    print(f'\n========== Result: {s} ==========')

def apply_burden(matrix):
    for i,j in np.ndindex(matrix.shape):
        if matrix[i][j] != 0:
            neighbors = getNeighbors(matrix, i, j)
            for r,c in neighbors:
                matrix = apply_burden_el(matrix, r, c)
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

def apply_burden_el(matrix, row,col):
    if (matrix[row][col] != 0):
        matrix[row][col] += 1  
    return matrix

def test():
    return
    
def main(debug=False):
    with open("day4/input.txt") as f:
        matrix = [list(line.strip()) for line in f]
        
    conv = {'.': 0, '@': 1}
    matrix_num = np.array([[conv[c] for c in row] for row in matrix])
    if debug: print(f'result : {matrix_num}')
    countAccessible(matrix_num, debug=debug)

if __name__ == '__main__':
    #test()
    main(True)

