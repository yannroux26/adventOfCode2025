from tokenize import String

def AddAll(banks,debug=False):
    s = 0
    for bank in banks:
        s += voltage(bank, debug=debug)
    print(f'Result: {s}')

def voltage(bank, debug=False):
    iMax1 = 0
    iMax2 = 1
    l = len(bank)
    for i in range(1,l-1):
        if bank[i] > bank[iMax1]:
            iMax1 = i
            iMax2 = i + 1
        elif bank[i] > bank[iMax2]:
            iMax2 = i
            
    if bank[l-1] > bank[iMax2]:
        iMax2 = l-1
    if debug:
        print(f'Bank: {bank} Max1: {bank[iMax1]} Max2: {bank[iMax2]}')
    return int(bank[iMax1]) * 10 + int(bank[iMax2])
    
def test():
    return
    
def main(debug=False):
    with open('day3/input.txt') as f:
        banks = f.read().split('\n')
    AddAll(banks, debug=debug)

if __name__ == '__main__':
    #test()
    main(True)

