#advent of code 1.1

Position = 50




# the position is between 0 and 100, so if it goes below 0, it wraps around to 100, and if it goes above 100, it wraps around to 0.
# move are composed of a direction (L or R) and a number of steps (e.g., L10 means move left 10 steps)
def nextPosition(current_position, move):
    if move[0] == 'L':
        current_position -= int(move[1:])
    elif move[0] == 'R':
        current_position += int(move[1:])
        
    current_position = current_position % 100
    if current_position < 0:
        current_position += 100
    return current_position