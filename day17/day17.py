import heapq
from dataclasses import dataclass, field
from input_util import parse_as_list_of_lines, read_demo, read_input

day = "day17"

DEBUG =  True

def log(*x, end="\n"):
    if DEBUG:
        print(*x, end=end)

def log_chamber(chamber, block=None):
    res = []

    max_y = max(max(c[1] for c in block.occupied())+1, len(chamber.occupied))
    res = [["."] * 7 for _ in range(max_y)]

    for y, row in enumerate(chamber.occupied):
        for x in row:
            res[y][x] = "#"

    if block:
        for x, y in block.occupied():
            if res[y][x] == "#":
                res[y][x] = "X"
            else:
                res[y][x] = "@"
        
    for r in reversed(res):
        log("|", end="")
        log("".join(r), end="")
        log("|")
    log("+-------+")
    log()

@dataclass(order=True)
class Block:
    def __init__(self, pos):
        self.pos = pos

    def shape(self):
        raise NotImplementedError

    def shift(self, d):
        self.pos[0] = self.pos[0] + d[0]
        self.pos[1] = self.pos[1] + d[1]
    
    def occupied(self):
        return [(x + self.pos[0], y + self.pos[1]) for x, y in self.shape()]

class Block0(Block):
    def shape(self):
        return [(0, 0), (1, 0), (2, 0), (3, 0)]

class Block1(Block):
    def shape(self):
        return [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]

class Block2(Block):
    def shape(self):
        return [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

class Block3(Block):
    def shape(self):
        return [(0, 0), (0, 1), (0, 2), (0, 3)]

class Block4(Block):
    def shape(self):
        return [(0, 0), (1, 0), (0, 1), (1, 1)]


class Chamber:
    def __init__(self):
        self.occupied = []

    def add_block(self, block):
        for x, y in block.occupied():
            while y >= len(self.occupied):
                self.occupied.append([])
            self.occupied[y].append(x)

    def can_move(self, block, d):
        block_occ = [(x[0] + d[0], x[1] + d[1]) for x in block.occupied()]
        for x, y in block_occ:
            if y < 0:
                return False
            if x < 0 or x >= 7:
                return False
            if 0 <= y < len(self.occupied) and x in self.occupied[y]:
                return False
        return True

    def get_top_y(self):
        return len(self.occupied)


def main(use_demo=False):

    if use_demo:
        air = read_demo(day)
    else:
        air = read_input(day)

    chamber = Chamber()
    blocks_cls = [Block0, Block1, Block2, Block3, Block4]

    ds = {">": (1, 0), "<": (-1, 0)}
    down = (0, -1)
    t = 0 # time
    n = 0 # number of block

    while n < 1000000000000:
        if n % 10000 == 0:
            log(n)
        top_y = chamber.get_top_y()
        b = blocks_cls[n%5]([2, top_y+3])
        # log_chamber(chamber, b)
        while True:
            d = ds[air[t%len(air)]]
            if chamber.can_move(b, d):
                b.shift(d)
            t += 1
            if not chamber.can_move(b, down):
                break
            b.shift(down)
        n += 1
        chamber.add_block(b)
    log(chamber.get_top_y())
