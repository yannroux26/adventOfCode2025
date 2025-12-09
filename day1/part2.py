#advent of code 1.1

testMoves = ['L600', 'R10', 'L30', 'R40', 'L50', 'R80']

def countZeros(moves, test=False):
    int = 0
    position = 50
    for move in moves:
        position, nb_turns = nextPosition(position, move, test=test)
        int += nb_turns
    print(f'Result: {int}')

def nextPosition(current_position, move, test=False):
    nb_crans = int(move[1:])
    nb_turns = nb_crans // 100
    nb_crans = nb_crans % 100
    currentNull = (current_position == 0)
    if nb_crans == 0 :
        return current_position, nb_turns
        
    
    if move[0] == 'L':
        current_position -= nb_crans
    elif move[0] == 'R':
        current_position += nb_crans

    if current_position < 0:
        current_position += 100
        if not currentNull:
            nb_turns += 1
    if current_position > 100:
        current_position -= 100
        nb_turns += 1
    if current_position == 100:
        current_position = 0
    
    if current_position == 0:
        nb_turns += 1
    
    if test :
        print(f'After move {move}, new position is {current_position}, number of turns: {nb_turns}')
    return current_position, nb_turns

def test():
    int = countZeros(testMoves, test=True)
    print(f'Test result: {int}')

def main(test=False):
    with open('day1/list_moves.txt') as f:
        moves = f.read().split('\n')
    result = countZeros(moves, test=test)

if __name__ == '__main__':
    #test()
    main(True)