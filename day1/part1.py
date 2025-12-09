#advent of code 1.1

testMoves = ['L60', 'R10', 'L30', 'R40', 'L50', 'R60']

def countZeros(moves, test=False):
    int = 0
    position = 50
    for move in moves:
        position = nextPosition(position, move, test=test)
        if position == 0:
            int += 1
    print(f'Result: {int}')

def nextPosition(current_position, move, test=False):
    if move[0] == 'L':
        current_position -= int(move[1:])
    elif move[0] == 'R':
        current_position += int(move[1:])
        
    current_position = current_position % 100
    if current_position < 0:
        current_position += 100
    if test :
        print(f'After move {move}, new position is {current_position}')
    return current_position

def test():
    int = countZeros(testMoves, test=True)
    print(f'Test result: {int}')

def main():
    with open('day1/list_moves.txt') as f:
        moves = f.read().split('\n')
    result = countZeros(moves)

if __name__ == '__main__':
    #test()
    main()