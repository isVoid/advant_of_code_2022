from functools import cmp_to_key
from input_util import parse_as_list_of_lines, read_demo, read_input

day = "day13"

DEBUG = True 

def log(*x):
    if DEBUG:
        print(*x)

def parse_line(line):
    i = 0
    stack = []
    cur = None 
    while i < len(line):
        if line[i] == '[':
            stack.append(cur)
            cur = []
            i += 1
        elif line[i].isdigit():
            j = i+1
            while line[i:j].isdigit():
                j += 1
            cur.append(int(line[i:j-1]))
            i = j-1
        elif line[i] == ',':
            i += 1
        elif line[i] == ']':
            if stack[-1] is not None:
                stack[-1].append(cur[:])
                cur = stack.pop()
            i += 1
        else:
            raise ValueError(f"Unexpected Token: {line[i]}")
    
    return cur

def compare(lhs, rhs):
    if isinstance(lhs, int) and isinstance(rhs, int):
        if lhs < rhs:
            return -1
        elif lhs == rhs:
            return 0
        else:
            return 1
    elif isinstance(lhs, list) and isinstance(rhs, list):
        i, j = 0, 0
        while i < len(lhs) and j < len(rhs):
            res = compare(lhs[i], rhs[j])
            if res < 0:
                return -1
            elif res > 0:
                return 1
            i += 1
            j += 1
        if len(lhs) == len(rhs):
            return 0
        elif len(lhs) < len(rhs):
            return -1
        else:
            return 1
    elif isinstance(lhs, list) and isinstance(rhs, int):
        return compare(lhs, [rhs])
    elif isinstance(lhs, int) and isinstance(rhs, list):
        return compare([lhs], rhs)
    else:
        raise ValueError(f"Unexpected input: {lhs}, {rhs}")


def main(use_demo=False):
    if use_demo:
        t = read_demo(day)
    else:
        t = read_input(day)
    
    lines = parse_as_list_of_lines(t)
    idx = 1
    packets = [[2], [6]]
    for i in range(0, len(lines), 3):
        left = parse_line(lines[i])
        right = parse_line(lines[i+1])
        packets += [left, right]

    packets = sorted(packets, key=cmp_to_key(compare))
    print(packets)

    res = 1
    for i, p in enumerate(packets):
        if compare(p, [2]) == 0 or compare(p, [6]) == 0:
            res *= i+1
    
    print(res)
