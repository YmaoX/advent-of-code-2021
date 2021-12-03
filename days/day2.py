def day2_1():
    with open("input/day2.txt") as fo:
        x = 0
        y = 0
        for line in fo:
            ss = line.split()
            value = int(ss[1])
            if ("forward" == ss[0]):
                x += value
            elif ("down" == ss[0]):
                y += value
            elif ("up" == ss[0]):
                y -= value
        return x, y, x*y

def day2_2():
    with open("input/day2.txt") as fo:
        aim = 0
        depth = 0
        horizontal = 0
        for line in fo:
            ss = line.split()
            value = int(ss[1])
            if ("forward" == ss[0]):
                horizontal += value
                depth = depth + aim * value
            elif ("down" == ss[0]):
                aim += value
            elif ("up" == ss[0]):
                aim -= value
        return aim, depth, horizontal, depth * horizontal