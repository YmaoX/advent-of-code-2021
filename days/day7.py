import math
import statistics


def get_input():
    fobj = open("input/day7.txt")
    line = fobj.readline().strip("\n")
    fobj.close()
    return list(map(int, line.split(",")))


def medians(l: list):
    l.sort()
    if len(l) % 2 == 0:
        return l[int(len(l)/2)], l[int(len(l)/2) + 1]
    return l[int(len(l)/2)]


def sum_distance(l: list, m: int):
    return sum(map(lambda i: abs(i - m), l))


def sum_distance2(l: list, m: int):
    return sum(map(lambda i: sum(range(abs(i - m) + 1)), l))


def part1():
    l = get_input()
    return min(sum_distance(l, m) for m in medians(l))


def part2():
    l = get_input()
    f = math.floor(statistics.mean(l))
    c = math.ceil(statistics.mean(l))
    fs = sum_distance2(l, f)
    cs = sum_distance2(l, c)
    return fs, cs, min(fs, cs)
