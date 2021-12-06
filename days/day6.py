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


# return self + sons
def process_fish(fish: int, days: int):
    new_days = days + (8 - fish)
    first = new_days - 9
    if first < 0:
        return 1

    son = 0
    while first >= 0:
        son += process_fish(8, first)
        first -= 7
    return 1 + son


# 362666
def part1():
    fishes = get_input()
    count = 0
    for fish in fishes:
        count += process_fish(fish, 80)
    return count


def part2():
    fishes = get_input()
    count = 0
    # for fish in fishes:
    #     count += process_fish(fish, 256)
    count = process_fish(fishes[0], 256)
    return len(fishes) + count
