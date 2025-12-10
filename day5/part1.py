import numpy as np
from tokenize import String

def countContained(intervals, ingredients, debug=False):
    count = 0
    for ingredient in ingredients:
        for interval in intervals:
            if contains(interval, int(ingredient), debug=debug):
                count += 1
                if debug:
                    print(f'Ingredient {ingredient} is contained in interval {interval}')
                break
            
    print(f'Total contained ingredients: {count}')

def contains(interval, ingredient, debug=False):
    return interval[0] <= ingredient <= interval[1]

def test():
    return
    
def main(debug=False):
    preIntervals = []
    ingredients = []
    with open("day5/input.txt") as f:
        for line in f:
            if line == "\n":
                break
            preIntervals.append(line.strip())
            
        for line in f:
            ingredients.append(line.strip())
    if debug:
        print(f'Intervals: {preIntervals}')
        print(f'Ingredients: {ingredients}')
    
    intervals = [(int(a), int(b)) for interval in preIntervals for a,b in [interval.split('-')]]
    
    # sort intervals by starting point
    intervals.sort(key=lambda x: x[0])
    if debug:
        print(f'Intervals as array:\n{intervals}')
        
    countContained(intervals, ingredients, debug=debug)

if __name__ == '__main__':
    #test()
    main()

