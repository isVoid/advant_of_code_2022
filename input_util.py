import os


def read_input(day, skip_strip=False):
    with open(os.path.join("inputs", day, "input.txt"), "r") as fn:
        t = fn.read()
    if not skip_strip:
        return t.strip()
    return t


def read_demo(day, skip_strip=False):
    with open(os.path.join("inputs", day, "demo.txt"), "r") as fn:
        t = fn.read()
    if not skip_strip:
        return t.strip()
    return t


def parse_as_list_of_lines(t):
    return t.splitlines()
