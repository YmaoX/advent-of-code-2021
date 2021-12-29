def get_input():
    fobj = open("input/day24.txt")
    ins = [l.strip("\n").split() for l in fobj.readlines()]
    fobj.close()
    return ins


monad = get_input()
var_list = set("wxyz")
block_size = 18
block_num = int(len(monad) / block_size)


def read_value(n, l):
    return int(monad[n * block_size + l][2])


def analyse():
    """
    w, x, y are all initialized in each block

    before step 7
    x = z % 26 + l6

    step 7: x == w -> x -> 0
    z = z / l5

    step 7: x != w -> x -> 1
    z = z / l5 * 26 + w + l16
    """
    for i in range(block_num):
        print(f"--------- block {i + 1} ---------")
        l6 = read_value(i, 5)
        print(f"x = z % 26 + {l6}")
        l5 = read_value(i, 4)
        print(f"if x != w, z = z / {l5} * 26 + w + {read_value(i, 15)}")
        # we can have another possibility
        if l6 <= 9 and l6 + 25 >= 1:
            print(f"if x == w, z = z / {l5}")
    """
    --------- block 1 ---------
    x = z % 26 + 14
    if x != w, z = z / 1 * 26 + w + 7
    --------- block 2 ---------
    x = z % 26 + 12
    if x != w, z = z / 1 * 26 + w + 4
    --------- block 3 ---------
    x = z % 26 + 11
    if x != w, z = z / 1 * 26 + w + 8
    --------- block 4 ---------
    x = z % 26 + -4
    if x != w, z = z / 26 * 26 + w + 1
    if x == w, z = z / 26
    --------- block 5 ---------
    x = z % 26 + 10
    if x != w, z = z / 1 * 26 + w + 5
    --------- block 6 ---------
    x = z % 26 + 10
    if x != w, z = z / 1 * 26 + w + 14
    --------- block 7 ---------
    x = z % 26 + 15
    if x != w, z = z / 1 * 26 + w + 12
    --------- block 8 ---------
    x = z % 26 + -9
    if x != w, z = z / 26 * 26 + w + 10
    if x == w, z = z / 26
    --------- block 9 ---------
    x = z % 26 + -9
    if x != w, z = z / 26 * 26 + w + 5
    if x == w, z = z / 26
    --------- block 10 ---------
    x = z % 26 + 12
    if x != w, z = z / 1 * 26 + w + 7
    --------- block 11 ---------
    x = z % 26 + -15
    if x != w, z = z / 26 * 26 + w + 6
    if x == w, z = z / 26
    --------- block 12 ---------
    x = z % 26 + -7
    if x != w, z = z / 26 * 26 + w + 8
    if x == w, z = z / 26
    --------- block 13 ---------
    x = z % 26 + -10
    if x != w, z = z / 26 * 26 + w + 4
    if x == w, z = z / 26
    --------- block 14 ---------
    x = z % 26 + 0
    if x != w, z = z / 26 * 26 + w + 6
    if x == w, z = z / 26
    
    => 
    for 7 of them, we have at least z = z * 26
    if we want to z == 0 at the end, we need to choose z = z / 26 for the other 7 blocks
    """


def process(model_range):
    zs = {0: ""}
    for i in range(block_num):
        new_zs = {}
        l5 = read_value(i, 4)
        l6 = read_value(i, 5)
        for w in model_range:
            if l6 <= 9 and l6 + 25 >= 1:
                for z, m in zs.items():
                    if z % 26 + l6 != w:
                        continue
                    k = int(z / l5)
                    new_zs[k] = m + str(w)
            else:
                l16 = read_value(i, 15)
                for z, m in zs.items():
                    k = int(z / l5) * 26 + w + l16
                    new_zs[k] = m + str(w)
        zs = new_zs
    print(zs)


def part1():
    process(range(9, 0, -1))


def part2():
    process(range(10))
