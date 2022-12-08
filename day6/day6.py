from collections import defaultdict

from input_util import parse_as_list_of_lines, read_demo, read_input

day = "day6"


def main(run_demo=True):
    if run_demo:
        t = read_demo(day)
    else:
        t = read_input(day)

    lines = parse_as_list_of_lines(t)

    window = 14

    for l in lines:
        c = defaultdict(int)
        for i in range(0, len(l)):
            c[l[i]] += 1
            if i < window:
                continue
            if i != window:
                c[l[i - window]] -= 1
            if max(c.values()) == 1:
                print(i + 1)
                break
