from functools import reduce
from input_util import parse_as_list_of_lines, read_demo, read_input

day = "day11"

DEBUG = False 

def log(*x):
    if DEBUG:
        print(*x)

class MonkeyManager:
    def __init__(self, monkeys):
        self.monkeys = monkeys
        for mk in self.monkeys:
            mk.mgr = self
        self.all_divisors = reduce(lambda p, x: p*x.divisible_by, self.monkeys, 1)
 
    def move(self, new_item, to_):
        # log(f"\tMove: item {old_item} from {from_} to {to_} as {new_item}")
        self.monkeys[to_].append(new_item)
    
    def eval(self):
        for i, mk in enumerate(self.monkeys):
            log(f"Monkey: {i}")
            log(mk.items)
            mk.eval()

class Monkey:
    def __init__(self, id_, items, op, divisible_by, true_move, false_move):
        self.id_ = id_
        self.items = items
        self.op = op
        self.divisible_by = divisible_by
        self.true_move = true_move
        self.false_move = false_move
        self.inspect_times = 0

    def append(self, item):
        self.items.append(item)
    
    def eval(self):
        """
        Use congruence relation here.
        https://en.wikipedia.org/wiki/Modular_arithmetic#Congruence

        The goal here is to check if `worry` w is divisible by 1 or more prime numbers n1, n2...
        aka, testing: is 0 ≡ w (mod n) ?
        `Worry` itself can be added or multiplied by some number.
        Storing the original number may result in a large number, which is too slow to process.
        Instead of storing the original number, only the remainder dividing the number by the
        product of all testing prime numbers is needed. This is because:

        if a ≡ b (mod n), then k*a ≡ k*b (mod k*n) for any integer k, and vice versa (k != 0)
        Consider `k` is the product of all other prime numbers except `n` - the number currently
        testing, if 0 ≡ k*w (mod k*n), then 0 ≡ w (mod n).

        What about preserving the test property above for arbitrary sequence of addition and
        multiplication? Not a problem, because congruence property is compatible with both ops.

        if a ≡ b (mod n), then        
        a + k ≡ b + k (mod n) for any integer k (compatibility with translation)
        k*a ≡ k*b (mod n) for any integer k (compatibility with scaling)

        This says, the remainder of b/n is a, then the remainder of the same divisor, but with
        adding k to b (or multiplied by) is the same as adding (or multiply) k to the remainder
        and taking the modulo of the result by n.

        In this way, the maximum number stored is always fewer than the product of all testing
        prime numbers, thus reducing the computation time.
        """
        self.inspect_times += len(self.items)
        for old in self.items:
            new = self.op(old) % self.mgr.all_divisors
            if new != 0 and new % self.divisible_by == 0:
                self.mgr.move(new, self.true_move)
            else:
                self.mgr.move(new, self.false_move)
        self.items = []


demo_monkey0 = Monkey(0, [79, 98], lambda x: x*19, 23, 2, 3)
demo_monkey1 = Monkey(1, [54, 65, 75, 74], lambda x: x+6, 19, 2, 0)
demo_monkey2 = Monkey(2, [79, 60, 97], lambda x:x*x, 13, 1, 3)
demo_monkey3 = Monkey(3, [74], lambda x:x+3, 17, 0, 1)

demo = [demo_monkey0, demo_monkey1, demo_monkey2, demo_monkey3]
demo_mgr = MonkeyManager(demo)

monkey0 = Monkey(0, [91, 66], lambda x: x*13, 19, 6, 2)
monkey1 = Monkey(1, [78, 97, 59], lambda x: x+7, 5, 0, 3)
monkey2 = Monkey(2, [57, 59, 97, 84, 72, 83, 56, 76], lambda x: x+6, 11, 5, 7)
monkey3 = Monkey(3, [81, 78, 70, 58, 84], lambda x: x+5, 17, 6, 0)
monkey4 = Monkey(4, [60], lambda x: x+8, 7, 1, 3)
monkey5 = Monkey(5, [57, 69, 63, 75, 62, 77, 72], lambda x: x*5, 13, 7, 4)
monkey6 = Monkey(6, [73, 66, 86, 79, 98, 87], lambda x: x*x, 3, 5, 2)
monkey7 = Monkey(7, [95, 89, 63, 67], lambda x: x+2, 2, 1, 4)

test = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]
mgr = MonkeyManager(test)

def main(use_demo=False):
    if use_demo:
        for rnd in range(10000):
            demo_mgr.eval()
            if rnd % 10 == 0:
                log(f"== After round {rnd} ==")
                for i, mk in enumerate(demo_mgr.monkeys):
                    log(f"Monkey {i} inspected items {mk.inspect_times} times.")
        for i, mk in enumerate(demo_mgr.monkeys):
            print(f"Monkey {i} inspected items {mk.inspect_times} times.")
    else:
        global mgr
        for _ in range(10000):
            mgr.eval()
        for i, mk in enumerate(mgr.monkeys):
            print(f"Monkey {i} inspected items {mk.inspect_times} times.")
    
    

