import math
from functools import reduce

non_nums = set('[],')


def get_input():
    fobj = open("input/day18.txt")
    lines = fobj.readlines()
    fobj.close()
    return [l.strip("\n") for l in lines]


def str_to_list(line: str):
    return [i if non_nums.__contains__(i) else int(i) for i in list(line)]


def process_list(l: list):
    e = s = True
    while e or s:
        n = level = 0
        for i in l:
            if i == ',':
                pass
            elif i == '[':
                if level == 4:
                    l = explode(l, n)
                    break
                else:
                    level += 1
            elif i == ']':
                level -= 1
            elif i >= 10 and not e:
                l = split(l, n)
                e = True
                break
            n += 1
        else:
            if e and s:
                e = False
            else:
                s = False

    return l


def explode(l: list, s: int):
    left = l[s + 1]
    right = l[s + 3]
    for i in range(s, -1, -1):
        if not non_nums.__contains__(l[i]):
            l[i] += left
            break
    for i in range(s + 4, len(l)):
        if not non_nums.__contains__(l[i]):
            l[i] += right
            break
    return l[0:s] + [0] + l[s+5:]


def split(l: list, s: int):
    sp = ['[', math.floor(l[s]/2), ',', math.ceil(l[s]/2), ']']
    return l[0:s] + sp + l[s+1:]


def add_line(l1: str, l2: str):
    return ['['] + str_to_list(l1) + [','] + str_to_list(l2) + [']']


def to_str(l: list):
    s = ""
    for i in l:
        if non_nums.__contains__(i):
            s += i
        else:
            s += str(i)
    return s


def magnitude(l: list):
    left = magnitude(l[0]) if isinstance(l[0], list) else l[0]
    right = magnitude(l[1]) if isinstance(l[1], list) else l[1]
    return 3 * left + 2 * right


def part1():
    lines = get_input()
    res = reduce(lambda a, b: to_str(process_list(add_line(a, b))), lines)
    print(magnitude(eval(res)))


def part2():
    lines = get_input()
    m = 0
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i != j:
                m = max(m, magnitude(eval(to_str(process_list(add_line(lines[i], lines[j]))))),
                        magnitude(eval(to_str(process_list(add_line(lines[j], lines[i]))))))
    print(m)
