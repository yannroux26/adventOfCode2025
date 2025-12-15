from itertools import count
import numpy as np

def main(debug=False):
    matrix = []
    with open("day7/input.txt") as f:
        matrix = [list(line.strip()) for line in f]
    
    rows, cols = len(matrix), len(matrix[0])

    for i in range(1,rows):
        for j in range(cols):
            up = matrix[i-1][j]
            if up == 'S':
                matrix[i][j] = 1
            elif up != '.' and up != '^' and up != 'S':
                if matrix[i][j] == '^':
                    matrix[i][j-1] = addC(matrix[i][j-1], up)
                    matrix[i][j+1] = addC(matrix[i][j+1], up)
                else :
                    matrix[i][j] = addC(matrix[i][j], up)

    if debug : print(np.array(matrix))
    print("========== result: " + str(sumLine(matrix[-1])) + " ==========")

def sumLine(line):
    s = 0
    for c in line:
        if c != '.' and c != '^' and c != 'S':
            s += int(c)
    return s
    
def addC(c, n):
    if c == '.':
        return n
    if n == '.':
        return c
    return int(c) + int(n)
                        

if __name__ == '__main__':
    main(True)