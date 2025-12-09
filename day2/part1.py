from tokenize import String

def AddAll(minMaxs, debug=False):
    s = 0
    for minMax in minMaxs:
        s += SumOfFalseIds(minMax, debug=debug)
    print(f'Result: {s}')


def SumOfFalseIds(minMax, debug=False):
    s = 0
    start, end = map(int, minMax.split('-'))
    if(debug):
        print(f'Processing minMax {start}-{end}')
    for n in range(start, end+1):
        if isDouble(n) :
            s += n
            if(debug):
                print(f'  Adding {n}')
    return s

def isDouble(n):
    s = str(n)
    if (len(s) % 2):
        return False
    l = len(s) / 2
    return (n % (1+10**l) == 0)
    

    
def main(debug=True):
    with open('day2/input.txt') as f:
        minMaxs = f.read().split(',')
    AddAll(minMaxs, debug=debug)

if __name__ == '__main__':
    #test()
    main(False)

