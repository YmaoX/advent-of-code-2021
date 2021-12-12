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


def run2(m: dict, start, visited: dict, s: str):
    count = 0
    for n in m[start]:
        if n == 'end':
            count += 1
        elif (visited.get(n, 0) != 0 and visited.get('used', False)) or n == 'start':
            continue
        elif n.islower():
            cp = copy.deepcopy(visited)
            cp[n] = cp.get(n, 0) + 1
            if cp[n] == 2:
                cp['used'] = True
            count += run2(m, n, cp, s + ',' + n)
        else:
            count += run2(m, n, visited, s + ',' + n)
    return count


def remove_after_visit(m: dict, c: str):
    if c.islower():
        cp = copy.deepcopy(m)
        for k, v in cp.items():
            v.discard(c)
    else:
        cp = m
    return cp


def part1():
    return run(get_input(), 'start')


def part2():
    return run2(get_input(), 'start', {}, 'start')
