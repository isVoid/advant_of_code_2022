import functools

from input_util import read_demo, read_input

day = "day3"


def parse_input(t):
    return t.splitlines()


def score(c):
    if ord(c) >= ord("a") and ord(c) <= ord("z"):
        return ord(c) - ord("a") + 1
    elif ord(c) >= ord("A") and ord(c) <= ord("Z"):
        return ord(c) - ord("A") + 27


def score_set(s):
    return sum(score(c) for c in s)


# def main():
#     # t = parse_input(read_demo(day))
#     t = parse_input(read_input(day))
#     res = 0
#     for l in t:
#         half = len(l) // 2
#         diff = set(l[:half]).intersection(set(l[half:]))
#         # print(diff)
#         for c in diff:
#             res += score(c)
#     print(res)


def group(rucks):
    for i in range(0, len(rucks), 3):
        yield rucks[i : i + 3]


def main():
    # t = parse_input(read_demo(day))
    t = parse_input(read_input(day))
    res = 0
    for g in group(t):
        sets = [set(r) for r in g]
        common = functools.reduce(lambda a, b: a.intersection(b), sets)
        res += score_set(common)
    print(res)
