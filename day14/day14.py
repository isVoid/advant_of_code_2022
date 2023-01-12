from input_util import parse_as_list_of_lines, read_demo, read_input

day = "day14"

DEBUG = True 

def log(*x):
    if DEBUG:
        print(*x)

def trace(b, e):
    if b[0] == e[0]:
        for y in range(min(b[1], e[1]), max(b[1], e[1])+1):
            yield (b[0], y)
    else:
        for x in range(min(b[0], e[0]), max(b[0], e[0])+1):
            yield (x, b[1])

def find(loc, occupied, floor_y):
    # log(loc, occupied)
    x, y = loc
    if y == floor_y:
        return (x, y-1)
    if (x, y+1) not in occupied:
        return find((x, y+1), occupied, floor_y)
    elif (x-1, y+1) not in occupied:
        return find((x-1, y+1), occupied, floor_y)
    elif (x+1, y+1) not in occupied:
        return find((x+1, y+1), occupied, floor_y)
    else:
        return (x, y)
    


def main(use_demo=False):
    if use_demo:
        t = read_demo(day)
    else:
        t = read_input(day)
    
    lines = parse_as_list_of_lines(t)

    occupied = set()
    for l in lines:
        coords = l.split('->')
        coords = [x.split(',') for x in coords]
        coords = [(int(x), int(y)) for x, y in coords]
        for b, e in zip(coords[:-1], coords[1:]):
            for c in trace(b, e):
                occupied.add(c)
    
    log(len(occupied))
    
    max_y = -1
    for x, y in occupied:
        max_y = max(max_y, y)
    floor = max_y + 2

    source = (500, 0)

    print(floor)

    res = 0
    loc = source
    while True:
        loc = find(source, occupied, floor)
        occupied.add(loc)
        res += 1
        if loc == source:
            break

    print(res)