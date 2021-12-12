import copy


def get_input():
    m = {}
    with open("input/day12.txt") as fo:
        for line in fo:
            cs = line.strip('\n').split("-")
            m.setdefault(cs[0], set()).add(cs[1])
            m.setdefault(cs[1], set()).add(cs[0])
    return m


def run(m: dict, start):
    count = 0
    for n in m[start]:
        if n == 'end':
            count += 1
        else:
            count += run(remove_after_visit(m, start), n)
    return count


def remove_after_visit(m: dict, c: str):
    cp = copy.deepcopy(m)
    if c.islower():
        for k, v in cp.items():
            v.discard(c)
    return cp


def part1():
    return run(get_input(), 'start')
