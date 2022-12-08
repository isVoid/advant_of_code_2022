from bisect import bisect_left
from enum import Enum

from input_util import parse_as_list_of_lines, read_demo, read_input

day = "day7"


class FsNode:
    def __init__(self, name: str, parent: "FsNode"):
        self.name = name
        self.parent = parent


class DirNode(FsNode):
    def __init__(self, name: str, parent: "DirNode", children: dict):
        super().__init__(name, parent)
        self.children = children

    def add_child(self, child: FsNode):
        self.children[child.name] = child

    def __str__(self):
        return f"{self.name} (Dir)"


class FileNode(FsNode):
    def __init__(self, name: str, parent: DirNode, size: int):
        super().__init__(name, parent)
        self.size = size

    def __str__(self):
        return f"{self.name} (File, size={self.size})"


root = DirNode("root", None, {})


def op_cd(cur, arg):
    if arg == "/":
        return root
    elif arg == "..":
        return cur.parent
    else:
        if arg not in cur.children:
            cur.add_child(DirNode(arg, cur, {}))
        return cur.children[arg]


def op_ls(cur, cmd):
    a, b = cmd.split()
    if a == "dir":
        if b not in cur.children:
            cur.add_child(DirNode(b, cur, {}))
    elif a.isnumeric():
        cur.add_child(FileNode(b, cur, int(a)))
    else:
        raise ValueError("Unepxected ls output: ", cmd)


rank = []


def dfs(cur, level):
    global rank
    print("  " * level + "- " + str(cur))
    if isinstance(cur, FileNode):
        return cur.size
    recursive_size = sum([dfs(child, level + 1) for child in cur.children.values()])
    rank.append((recursive_size, cur.name))
    return recursive_size


def main(with_demo=False):
    if with_demo:
        t = read_demo(day)
    else:
        t = read_input(day)

    cur = root

    cmds = parse_as_list_of_lines(t)

    state = 0
    i = 0

    while i < len(cmds):
        cmd = cmds[i]
        if state == 0:
            if cmd[2:4] == "cd":
                op, arg = "cd", cmd[5:]
            elif cmd[2:4] == "ls":
                op, arg = "ls", None

            if op == "cd":
                cur = op_cd(cur, arg)
            elif op == "ls":
                state = 1
            i += 1
        elif state == 1:
            if cmds[i][0] == "$":
                state = 0
            else:
                op_ls(cur, cmd)
                i += 1

    used = dfs(root, 0)
    unused = 70000000 - used
    need = 30000000
    diff = need - unused

    rank.sort(key=lambda x: x[0])
    # Needs 3.10
    # i = bisect_left(rank, diff, key=lambda x: x[0])
    for i, (size, name) in enumerate(rank):
        if size >= diff:
            break
    print(size, name)
