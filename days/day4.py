def get_input(lines: list):
    return [int(s) for s in lines[0].split(',')]


def get_boards(lines: list):
    boards = []
    i = 2
    while i < len(lines):
        board = []
        for j in range(0, 5):
            board.append([int(s) for s in lines[i + j].split()])
        boards.append(board)
        i += 6
    return boards


def get_input_and_boards():
    fobj = open("input/day4.txt")
    lines = fobj.readlines()
    ins = get_input(lines)
    boards = get_boards(lines)
    fobj.close()
    return ins, boards


def transpose(matrix):
    return [*zip(*matrix)]


def index_board(board: list, ins: list):
    bb = []
    for i in range(0, len(board)):
        bb.append([])
        for j in range(0, len(board[i])):
            index = -1
            try:
                index = ins.index(board[i][j])
            except ValueError:
                continue
            bb[i].append(index)
    return bb


def steps_for_board(board: list):
    row_min = min(list(map(max, board)))
    ts = transpose(board)
    col_min = min(list(map(max, ts)))
    return min(row_min, col_min)


def calculate(board: list, idx_board: list, final_input: int, final_index: int):
    print(board)
    print(idx_board)
    print(final_input)
    print(final_index)
    ss = 0
    for i in range(0, len(idx_board)):
        for j in range(0, len(idx_board[i])):
            if idx_board[i][j] > final_index or idx_board[i][j] == -1:
                ss += board[i][j]

    return ss * final_input


def day4_1():
    (ins, boards) = get_input_and_boards()
    bb = []
    for board in boards:
        bb.append(index_board(board, ins))

    min_v = -1
    idx = -1
    for i in range(0, len(bb)):
        m = steps_for_board(bb[i])
        if min_v == -1 or m < min_v:
            min_v = m
            idx = i
    return calculate(boards[idx], bb[idx], ins[min_v], min_v)


def day4_2():
    (ins, boards) = get_input_and_boards()
    bb = []
    for board in boards:
        bb.append(index_board(board, ins))

    max_v = -1
    idx = -1
    for i in range(0, len(bb)):
        m = steps_for_board(bb[i])
        if max_v == -1 or m > max_v:
            max_v = m
            idx = i
    return calculate(boards[idx], bb[idx], ins[max_v], max_v)
