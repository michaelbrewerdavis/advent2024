def parse(lines):
    return [line.strip() for line in lines]


def checkSpan(input, target, row, col, dir):
    dxs, dys = dir
    try:
        for dx, dy, target_char in zip(dxs, dys, target):
            x = col + dx
            y = row + dy
            if x < 0 or y < 0 or x >= len(input[0]) or y >= len(input):
                raise IndexError
            input_char = input[y][x]
            if input_char != target_char:
                return False
            # print(row, col, dx, dy, target_char, x, y, input_char)
        return True
    except IndexError:
        return False


TARGET = "XMAS"
LEN = len(TARGET)
DOWN = [[0] * LEN, range(0, LEN)]
RIGHT = [range(0, LEN), [0] * LEN]
LEFT = [range(0, -LEN, -1), [0] * LEN]
UP = [[0] * LEN, range(0, -LEN, -1)]
SE = [range(0, LEN, 1), range(0, LEN, 1)]
SW = [range(0, -LEN, -1), range(0, LEN, 1)]
NE = [range(0, LEN, 1), range(0, -LEN, -1)]
NW = [range(0, -LEN, -1), range(0, -LEN, -1)]
XMAS_ALL = [DOWN, RIGHT, LEFT, UP, SE, SW, NE, NW]


def checkXmas(input, row, col, dir):
    return checkSpan(input, TARGET, row, col, dir)


X_TARGET = "MAS"
SE = [range(-1, 2, 1), range(-1, 2, 1)]
NE = [range(-1, 2, 1), range(1, -2, -1)]
SW = [range(1, -2, -1), range(-1, 2, 1)]
NW = [range(1, -2, -1), range(1, -2, -1)]


def checkMas(input, row, col):
    if (
        checkSpan(input, X_TARGET, row, col, SE)
        or checkSpan(input, X_TARGET, row, col, NW)
    ) and (
        checkSpan(input, X_TARGET, row, col, SW)
        or checkSpan(input, X_TARGET, row, col, NE)
    ):
        return True
    return False


def run(input):
    print(
        len(
            [
                1
                for dir in XMAS_ALL
                for row, line in enumerate(input)
                for col, _cell in enumerate(line)
                if checkXmas(input, row, col, dir)
            ]
        )
    )
    print(
        len(
            [
                1
                for row, line in enumerate(input)
                for col, _cell in enumerate(line)
                if checkMas(input, row, col)
            ]
        )
    )
