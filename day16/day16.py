import re
from input_util import parse_as_list_of_lines, read_demo, read_input

day = "day16"

DEBUG =  True

def log(*x):
    if DEBUG:
        print(*x)

def floyd_warshall(graph, node2neighbors, node2id):
    for vi, i in node2id.items():
        for vj, j in node2id.items():
            if i == j:
                graph[i][j] = 0
            elif vj in node2neighbors[vi]:
                graph[i][j] = 1
            else:
                graph[i][j] = float('inf')
    
    V = len(graph)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


def main(use_demo=False):

    if use_demo:
        t = read_demo(day)
    else:
        t = read_input(day)
    
    lines = parse_as_list_of_lines(t)

    node2neighbors = dict()
    id2rate = dict()
    node2id = dict()
    indices = dict()

    p = r"Valve ([A-Z]*) has flow rate=(\d*); tunnels? leads? to valves? (.*)"
    for l in lines:
        m = re.match(p, l)
        node = m[1]
        node2id[node] = len(node2id)
        rate = int(m[2])
        neighbors = [x.strip() for x in m[3].split(",")]
        node2neighbors[node] = neighbors
        id2rate[node2id[node]] = rate
        indices[node2id[node]] = 1 << node2id[node]



    V = len(node2id)
    graph = [[0 for _ in range(V)] for _ in range(V)] 
    floyd_warshall(graph, node2neighbors, node2id)

    def dfs(i, t, state, flow, answer):
        """
        Inspired by:
        https://github.com/juanplopes/advent-of-code-2022/blob/main/day16.py
        https://www.reddit.com/r/adventofcode/comments/zn6k1l/comment/j0loibz/
        The key idea is using bitmask to represent visited nodes.
        """ 
        answer[state] = max(answer.get(state, 0), flow)
        for j in id2rate:
            nt = t-graph[i][j]-1
            if indices[j] & state or nt <= 0 or id2rate[j] == 0: continue
            dfs(j, nt, state | indices[j], flow+nt*id2rate[j], answer)
        return answer

    # part1 = dfs(node2id["AA"], 30, 0, 0, {})
    # print(max(part1.values()))
    res = dfs(node2id["AA"], 26, 0, 0, {})
    part2 = max(v1+v2 for k1, v1 in res.items() for k2, v2 in res.items() if not k1 & k2)
    print(part2)

    
    
 