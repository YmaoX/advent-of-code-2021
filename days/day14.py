import collections
import math
from collections import Counter


def get_input():
    rules = {}
    fobj = open("input/day14.txt")
    lines = fobj.readlines()
    s = lines[0].strip('\n')
    for line in lines[2:]:
        ss = line.strip('\n').split(" -> ")
        rules[ss[0]] = ss[1]
    fobj.close()

    return ["".join(t) for t in zip(list(s), list(s)[1:])], rules


def to_count(i: list):
    return dict(Counter(i))


def process(i: dict, rs: dict):
    n = {}
    for k, v in i.items():
        if k in rs:
            to = rs.get(k)
            l = list(k)
            n_1 = l[0] + to
            n_2 = to + l[1]
            n[n_1] = n.get(n_1, 0) + v
            n[n_2] = n.get(n_2, 0) + v
    return n


def count_m(m: dict):
    n = {}
    for k, v in m.items():
        for i in k:
            n[i] = n.get(i, 0) + v
    return math.ceil(min(n.values()) / 2), math.ceil(max(n.values()) / 2)


def part(n: int):
    i, rs = get_input()
    c = to_count(i)
    for i in range(n):
        c = process(c, rs)
    a, b = count_m(c)
    print(b - a)
