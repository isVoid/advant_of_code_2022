from input_util import parse_as_list_of_lines, read_demo, read_input

day = "day10"

book = {20, 60, 100, 140, 180, 220}


def main(use_demo=False):
    if use_demo:
        t = read_demo(day)
    else:
        t = read_input(day)

    lines = parse_as_list_of_lines(t)

    X = 1

    state = 0
    res = 0
    oprnd = None
    cmds = list(reversed(lines))
    for clock in range(1, 241):
        if len(cmds) == 0:
            break

        curpix = (clock - 1) % 40
        if curpix == 0:
            print()

        if curpix >= X - 1 and curpix <= X + 1:
            print("#", end="")
        else:
            print(".", end="")

        # if clock in book:
        #     res += clock * X

        if state == 0:
            cmd = cmds.pop()
            if cmd == "noop":
                continue
            if cmd.startswith("addx"):
                state = 1
                oprnd = int(cmd.split()[1])
        elif state == 1:
            X += oprnd
            state = 0
