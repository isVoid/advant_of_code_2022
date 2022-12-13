import numpy as np
from input_util import parse_as_list_of_lines, read_demo, read_input

day = "day8"


def scan(val, arr, reversed=False):
    if len(arr) == 0:
        return 0
    res = 0
    for k in arr if not reversed else arr[::-1]:
        res += 1
        if k >= val:
            break
    return res


def main(use_demo=False):
    if use_demo:
        t = read_demo(day)
    else:
        t = read_input(day)

    lines = parse_as_list_of_lines(t)
    grid = np.asarray([[int(x) for x in l] for l in lines])

    best = 0
    loc = None
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            res = scan(grid[i, j], grid[i, :j], reversed=True)
            res *= scan(grid[i, j], grid[i, j + 1 :])
            res *= scan(grid[i, j], grid[:i, j], reversed=True)
            res *= scan(grid[i, j], grid[i + 1 :, j])
            if res > best:
                best = max(best, res)
                loc = (i, j)

    print(best)
    print(loc)
