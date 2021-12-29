import itertools
import re


def get_input():
    r = r'Player (?:\d+) starting position: (\d+)\n'
    fobj = open("input/day21.txt")
    lines = fobj.readlines()
    fobj.close()
    return [int(re.search(r, l).groups()[0]) for l in lines]


def play(score, position, steps_sum):
    new_p = (position + steps_sum) % 10
    new_s = score + (10 if new_p == 0 else new_p)
    return new_s, new_p


def get_next(last_end, limit):
    steps = []
    for i in range(1, 4):
        n = (last_end + i) % limit
        steps.append(limit if n == 0 else n)
    return steps


def part1():
    p1, p2 = get_input()
    goal = 1000
    p1s = p2s = 0
    steps = [0, 0, 0]
    c = 0
    while True:
        steps = get_next(steps[-1], 100)
        p1s, p1 = play(p1s, p1, sum(steps))
        c += 3
        if p1s >= goal:
            break

        steps = get_next(steps[-1], 100)
        p2s, p2 = play(p2s, p2, sum(steps))
        c += 3
        if p2s >= goal:
            break
    print(c * min(p1s, p2s))


def part2():
    def play_2(p1, s1, p2, s2):
        k = (p1, p2, s1, s2)
        if k in cache:
            return cache[k]
        winning = [0, 0]
        for i in d:
            new_s1, new_p1 = play(s1, p1, i)
            if new_s1 >= 21:
                winning[0] += 1
            else:
                a, b = play_2(p2, s2, new_p1, new_s1)
                winning[0] += b
                winning[1] += a
        cache[k] = winning
        return winning

    vs = (1, 2, 3)
    d = [sum(i) for i in list(itertools.product(vs, vs, vs))]
    p1, p2 = get_input()
    cache = {}

    print(max(play_2(p1, 0, p2, 0)))
