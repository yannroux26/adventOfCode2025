from itertools import count
import numpy as np

def main(debug=False):
    positions = []
    with open("day9/input.txt") as f:
        positions = np.array([line.strip().split(',') for line in f])
    
    max_area = 0
    for i in range(len(positions)):
        for j in range(i):
            current_area = area(positions[i], positions[j])
            if current_area > max_area:
                max_area = current_area
    
    print(max_area)
    
    
def area(pos1, pos2):
    a = abs(int(pos1[0]) - int(pos2[0])) + 1
    b = abs(int(pos1[1]) - int(pos2[1])) + 1
    return a * b    

if __name__ == '__main__':
    main()