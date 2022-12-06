from input_util import parse_as_list_of_lines, read_demo, read_input

day = "day4"


def as_pair_of_ranges(lines):
    for l in lines:
        first, second = l.split(",")
        first_pair = list(int(x) for x in first.split("-"))
        second_pair = list(int(x) for x in second.split("-"))
        yield (first_pair, second_pair)


def main():
    # lines = parse_as_list_of_lines(read_demo(day))
    lines = parse_as_list_of_lines(read_input(day))
    res = 0
    for p in as_pair_of_ranges(lines):
        first, second = p
        l = [(first[0], 0), (first[1], 0), (second[0], 1), (second[1], 1)]
        l = sorted(l, key=lambda x: x[0])
        if l[1][0] == l[2][0]:
            res += 1
            continue
        for i in range(0, len(l), 2):
            if l[i][1] != l[i + 1][1]:
                res += 1
                break
    print(res)
