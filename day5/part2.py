import numpy as np
from tokenize import String

def countEl(intervals, debug=False):
    total = 0
    for interval in intervals:
        total += interval[1] - interval[0] + 1
    print(f'Total elements in grouped intervals: {total}')

def groupIntervals(intervals, debug=False):
    grouped = []
    min1, max1 = intervals[0]
    
    for min2, max2 in intervals[1:]:
        if min2 <= max1:
            max1 = max(max1, max2)
        else:
            grouped.append((min1, max1))
            min1, max1 = min2, max2
            
    grouped.append((min1, max1))
    if debug:
        print(f'Grouped intervals: {grouped}')
    return grouped

def test():
    return
    
def main(debug=False):
    preIntervals = []
    with open("day5/input.txt") as f:
        for line in f:
            if line == "\n":
                break
            preIntervals.append(line.strip())

    if debug:
        print(f'Intervals: {preIntervals}')
    
    intervals = [(int(a), int(b)) for interval in preIntervals for a,b in [interval.split('-')]]
    
    # sort intervals by starting point
    intervals.sort(key=lambda x: x[0])
    if debug:
        print(f'Intervals as array:\n{intervals}')
        
    grouped_intervals = groupIntervals(intervals, debug=debug)
    countEl(grouped_intervals, debug=debug)

if __name__ == '__main__':
    #test()
    main()