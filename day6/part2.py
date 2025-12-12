def computeLine(lines, nbRead, debug):
    l = len(lines)
    sign = lines[-1][-1-nbRead]
    nbDigit = 1
    
    # parse to find the sign and numbers of digits
    while sign ==' ':
        nbDigit += 1
        sign = lines[-1][-nbDigit-nbRead]
    if debug: print(f'Found sign: {sign} after {nbDigit} digits')
    
    # extract numbers
    numbers = []
    for i in range(nbDigit):
        digits = []
        for j in range(l-1):
            c = lines[j][-i -nbRead -1]
            #if debug: print(f'line {j} char: {c} is read')
            if c != ' ':
                digits.append(int(c))    
        
        number = 0
        for j in range(len(digits)):
            number = number*10 + digits[j]
        numbers.append(number)
    if debug: print(f'Numbers: {numbers} with sign {sign}')
    
    # compute calcul
    isPlus = (sign=='+')
    val = numbers[0]
    for i in range(1,len(numbers)):
        if debug: print(f'  val : {val} {sign} {numbers[i]}')
        if isPlus:
            val += numbers[i]
        else:
            val *= numbers[i]
    
    nbRead += nbDigit + 1
    if debug: print(f'Computed value: {val} after reading {nbRead} characters')
    return val, nbRead

def SumLine(lines, debug):
    s = 0
    nbRead = 1 # to skip the \n
    l = len(lines[0])
    while nbRead < l:
        val, nbRead = computeLine(lines, nbRead, debug)
        s += val
    print(f'\n========== Result: {s} ==========')
    
def main(debug=False):
    lines = []
    with open("day6/input.txt") as f:
        for line in f:
            lines.append(line)
    SumLine(lines, debug)


if __name__ == '__main__':
    main(True)