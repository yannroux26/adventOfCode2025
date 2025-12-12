import numpy as np
from tokenize import String

def SumLine(lines, signs, debug):
    s = 0
    for i in range(lines.shape[0]):
        s += computeLine(lines[i], signs[i], debug)
    print(f'\n========== Result: {s} ==========')

def computeLine(line, sign, debug):
    isPlus = (sign=='+')
    val = line[0]
    for i in range(1,len(line)):
        if debug: print(f'  val : {val} {sign} {line[i]}')
        if isPlus:
            val += line[i]
        else:
            val *= line[i]
    
    if debug: print(f'Line: {line} with sign {sign} => {val}')
    return val
    
def main(debug=False):
    tab = []
    with open("day6/input.txt") as f:
        for line in f:
            tab.append([(int(x) if x.isdigit() else x) for x in line.strip().split()])
    
    matrix = np.array(tab[:-1]).transpose()      
    signs = tab[-1]
    
    if debug: print(f'result :\n{matrix} \n signs: {signs}')
    SumLine(matrix, signs, debug)
    
    print(57228996 * 72)

if __name__ == '__main__':
    main(True)