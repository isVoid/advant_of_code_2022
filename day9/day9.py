from input_util import parse_as_list_of_lines, read_demo, read_input

day = "day9"

hloc_dirs = {"R": (1, 0), "L": (-1, 0), "D": (0, -1), "U": (0, 1)}

"""
0 1 2
3 4 5
6 7 8
"""
transition = {
    0: {"R": (3, (1, -1)), "L": (1, (0, 0)), "D": (1, (1, -1)), "U": (3, (0, 0))},
    1: {"R": (0, (0, 0)), "L": (2, (0, 0)), "D": (1, (0, -1)), "U": (4, (0, 0))},
    2: {"R": (1, (0, 0)), "L": (5, (-1, -1)), "D": (1, (-1, -1)), "U": (5, (0, 0))},
    3: {"R": (3, (1, 0)), "L": (4, (0, 0)), "D": (0, (0, 0)), "U": (6, (0, 0))},
    4: {"R": (3, (0, 0)), "L": (5, (0, 0)), "D": (1, (0, 0)), "U": (7, (0, 0))},
    5: {"R": (4, (0, 0)), "L": (5, (-1, 0)), "D": (2, (0, 0)), "U": (8, (0, 0))},
    6: {"R": (3, (1, 1)), "L": (7, (0, 0)), "D": (3, (0, 0)), "U": (7, (1, 1))},
    7: {"R": (6, (0, 0)), "L": (8, (0, 0)), "D": (4, (0, 0)), "U": (7, (0, 1))},
    8: {"R": (7, (0, 0)), "L": (5, (-1, 1)), "D": (5, (0, 0)), "U": (7, (-1, 1))},
}


def main(use_demo=False):
    if use_demo:
        t = read_demo(day, skip_strip=True)
    else:
        t = read_input(day, skip_strip=True)

    cmds = parse_as_list_of_lines(t)

    tlocs = set()
    hlocs = [(0, 0)] * 10
    states = [4] * 10

    for cmd in cmds:
        d, n = cmd.split()
        n = int(n)
        while n != 0:
            hloc[0] = (hloc[0][0] + hloc_dirs[d][0], hloc[0][1] + hloc_dirs[d][1])
            for i in range(1, 10):
                hloc = hlocs[i]
                tstate, step = transition[tstate][d]
                hloc = (hloc[0] + step[0], hloc[1] + step[1])
            n -= 1
    print(len(tlocs))
