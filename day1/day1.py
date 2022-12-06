import os

day = "day1"


def read_input(filename):
    with open(os.path.join("inputs", day, filename), "r") as fn:
        t = fn.read()
    return t.strip()


def parse_input(txt):
    grp = txt.split("\n\n")
    res = []
    for g in grp:
        d = [int(x) for x in g.split("\n")]
        res.append(d)
    return res


def impl1(case):
    cal = parse_input(read_input(case))
    return max(sum(x) for x in cal)


def impl2(case):
    cal = parse_input(read_input(case))
    sumcal = [sum(x) for x in cal]
    return sum(sorted(sumcal, reverse=True)[0:3])


def test_demo():
    r = impl1("demo.txt")
    print(r)


def test_p1():
    r = impl1("1.txt")
    print(r)


def test_p2():
    r = impl2("1.txt")
    print(r)


# test_p1()
test_p2()
