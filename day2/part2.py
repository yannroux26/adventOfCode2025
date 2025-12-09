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
        if isRepeted(n) :
            s += n
            if(debug):
                print(f'  Adding {n}')
    return s

def isRepeted(n):
    s = str(n)
    lenN = len(s)
    for p in range(2, lenN+1):
        if (lenN % p) == 0:
            if isPRepeted(n, p):
                return True
    return False

def isPRepeted(n, nbRep):
    lenN = len(str(n))
    lenSeg = lenN // nbRep
    diviser = 1
    #print(f'Checking if {n} has {nbRep} repeted segments of length {lenSeg}')
    for i in range(nbRep-1):
        diviser = diviser*(10**lenSeg)+1
    #print(f'Diviser for p={nbRep} and n={n} is {diviser}')
    return (n % diviser == 0)
    
def test():
    print(f'result : {isPRepeted(123123, 3)}')
    print(f'result : {isPRepeted(141414, 3)}')
    print(f'result : {isPRepeted(123123, 2)}')
    print(f'result : {isPRepeted(141414, 2)}')
    print(f'result : {isPRepeted(141414, 6)}')
    print(f'result : {isPRepeted(111111, 6)}')
    
    
def main(debug=True):
    with open('day2/input.txt') as f:
        minMaxs = f.read().split(',')
    AddAll(minMaxs, debug=debug)

if __name__ == '__main__':
    #test()
    main(True)

