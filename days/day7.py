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


def part1():
    l = get_input()
    return min(sum_distance(l, m) for m in medians(l))

