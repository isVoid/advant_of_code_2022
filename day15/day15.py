import re
import bisect
from functools import cmp_to_key
from input_util import parse_as_list_of_lines, read_demo, read_input

day = "day15"

DEBUG =  False

def log(*x):
    if DEBUG:
        print(*x)

def manhatten(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def merge_intervals(intervals, new_intvl):
    intervals.append(new_intvl)
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if len(merged) == 0 or merged[-1][1] < interval[0]-1:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
    

class Map:
    def __init__(self, minc, maxc):
        self._d = dict()
        self.minx, self.maxx = minc, maxc
        self.miny, self.maxy = minc, maxc
    
    def add_interval(self, y, minx, maxx):
        if y < self.miny or y > self.maxy:
            return

        minx = max(minx, self.minx)
        maxx = min(maxx, self.maxx)

        if y not in self._d:
            self._d[y] = [[minx, maxx]]
        else:
            self._d[y] = merge_intervals(self._d[y], [minx, maxx])

    def get_y(self, y):
        if y not in self._d:
            return []
        return self._d[y]

def count_occupied(intervals):
    return sum(intvl[1]-intvl[0] for intvl in intervals)

def main(use_demo=False):
    if use_demo:
        t = read_demo(day)
    else:
        t = read_input(day)
    
    lines = parse_as_list_of_lines(t)

    regex = r"Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)"

    map_ = Map(0, 4000000)
    for l in lines:
        print(l)
        m = re.match(regex, l)
        sx, sy, bx, by = [int(x) for x in [m[1], m[2], m[3], m[4]]]
        d = manhatten((sx, sy), (bx, by))
        for y in range(sy-d, sy+d+1):
            r = d-abs(y-sy)
            map_.add_interval(y, sx-r, sx+r)
    
    for y in range(0, 4000000):
        if len(map_.get_y(y)) == 2:
            print(y+4000000*(map_.get_y(y)[0][1]+1))

    




        
