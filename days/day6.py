from collections import Counter


def get_input():
    fobj = open("input/day6.txt")
    line = fobj.readline().strip("\n")
    fobj.close()
    return list(map(int, line.split(",")))


def process_day(fishes: list):
    for i in range(len(fishes)):
        if fishes[i] == 0:
            fishes.append(8)
            fishes[i] = 6
        else:
            fishes[i] -= 1


# 362666
def part1():
    fishes = get_input()
    count = 0
    for fish in fishes:
        count += process_day(fish, 80)
    return count


def part2():
    fishes = get_input()
    lifes = dict(Counter(fishes))
    for day in range(256):
        lifes = {l - 1: lifes.get(l, 0) for l in range(0, 9)}
        lifes[8] = lifes[-1]
        lifes[6] += lifes[-1]
        lifes[-1] = 0

    return sum(lifes.values())
