from tokenize import String

def AddAll(banks,debug=False):
    s = 0
    for bank in banks:
        s += voltage(bank, debug=debug)
    print(f'Result: {s}')

def voltage(bank, debug=False):
    iMax = [i for i in range(12)] # 12 indexes with a value between 0 and len(bank)-1
    lenBank = len(bank)
    for ib in range(1,lenBank):
        iMax = compWithAll(bank, ib, 0, iMax,lenBank, debug=debug)
    
    if debug:
        print(f'Bank: {bank} => iMax: {iMax}')
        print(f'Values: {[bank[i] for i in iMax]}')
    
    s = 0
    for i in range(12):
        s += int(bank[iMax[i]]) * (10 ** (11 - i))
    return s

def compWithAll(bank, ib, iim, iMax,lenBank, debug=False):
    # first cases :
    if iMax[iim] == ib :
        return iMax
    
    # last cases :
    if lenBank -12 +iim < ib :
        return compWithAll(bank, ib, iim + 1, iMax,lenBank, debug=debug)
    
    if bank[ib] > bank[iMax[iim]]:
        iMax[iim] = ib
        if iim != 12 :
            iMax = UpdateAllIMax(iMax, iim)
        return iMax
    else : 
        if iim != 11 :
            return compWithAll(bank, ib, iim + 1, iMax,lenBank, debug=debug)
        return iMax

def UpdateAllIMax(iMax,i):
    val = iMax[i]
    for j in range(i+1, len(iMax)):
        iMax[j] = val + j - i
    return iMax
    
def test():
    return
    
def main(debug=False):
    with open('day3/input.txt') as f:
        banks = f.read().split('\n')
    AddAll(banks, debug=debug)

if __name__ == '__main__':
    #test()
    main(False)

