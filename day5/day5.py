import re

from input_util import read_demo, read_input

day = "day5"

run = "input"


def main():
    if run == "demo":
        t = read_demo(day, skip_strip=True)
    else:
        t = read_input(day, skip_strip=True)

    stacks, ops = t.split("\n\n")

    l = stacks.split("\n")
    num_stacks = len(l[-1].split())

    stack_as_deque = [[] for _ in range(num_stacks)]
    for line in l[:-1]:
        i = 0
        while i < len(line):
            if line[i : i + 3] != "   ":
                stack_as_deque[i // 4].append(line[i : i + 3].strip("[]"))
            i += 4

    stack_as_deque = [list(reversed(s)) for s in stack_as_deque]

    ops = ops.split("\n")
    for op in ops[:-1]:
        # print(op)
        opdict = re.match(
            r"move (?P<num_block>\d*) from (?P<from>\d) to (?P<to>\d)", op
        ).groupdict()
        opdict = {k: int(v) for k, v in opdict.items()}
        buffer = []
        for _ in range(opdict["num_block"]):
            buffer.append(stack_as_deque[opdict["from"] - 1].pop())
        buffer = list(reversed(buffer))
        stack_as_deque[opdict["to"] - 1] += buffer

    res = "".join(l[-1] for l in stack_as_deque)
    print(res)
