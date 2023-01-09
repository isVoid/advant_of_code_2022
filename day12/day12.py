from collections import deque
from input_util import parse_as_list_of_lines, read_demo, read_input

day = "day12"

DEBUG = True 

def log(*x):
    if DEBUG:
        print(*x)

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(grid, start):
    # Part2
    q = deque()
    visited = set()

    q.append(start)
    step = 0
    while len(q) > 0:
        length = len(q)
        while length > 0:
            i, j = q.popleft()
            if grid[i][j] == 'a':
                return step

            visited.add((i, j))
            for d in dir:
                ni, nj = i + d[0], j + d[1]
                if (ni >= 0 and ni < len(grid) and 
                    nj >= 0 and nj < len(grid[0]) and 
                    (ni, nj) not in visited and 
                    (ord(grid[ni][nj]) - ord(grid[i][j])) >= -1):
                    visited.add((ni, nj))
                    q.append((ni, nj))
            length -= 1
        step += 1

def main(use_demo=False):
    global Ei, Ej

    if use_demo:
        t = read_demo(day)
    else:
        t = read_input(day)
    
    grid = parse_as_list_of_lines(t)
    grid = [list(line) for line in grid]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                grid[i][j] = 'a'
            if grid[i][j] == 'E':
                Si, Sj = i, j
                grid[i][j] = 'z'

    n = bfs(grid, (Si, Sj))
    print(n)
    

