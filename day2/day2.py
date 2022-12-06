from input_util import read_demo, read_input

day = "day2"

# d = {
#     "A X": 4,
#     "A Y": 8,
#     "A Z": 3,
#     "B X": 1,
#     "B Y": 5,
#     "B Z": 9,
#     "C X": 7,
#     "C Y": 2,
#     "C Z": 6,
# }

d = {
    "A X": 3,  # R S Lose
    "A Y": 4,  # R R Draw
    "A Z": 8,  # R P Win
    "B X": 1,  # P R Lose
    "B Y": 5,  # P P Draw
    "B Z": 9,  # P S Win
    "C X": 2,  # S P Lose
    "C Y": 6,  # S S Draw
    "C Z": 7,  # S R Win
}


def p1():
    # t = read_demo(day)
    t = read_input(day)
    t = t.splitlines()
    return sum(d[l] for l in t)


def main():
    print(p1())
