from copy import deepcopy


class CycleException(Exception):
    pass


def parse(lines):
    return [list(line.strip()) for line in lines]


def advance(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])


def turnRight(dir):
    return (-dir[1], dir[0])


def findStart(board):
    height = len(board)
    width = len(board[0])
    return next(
        (a, b) for b in range(height) for a in range(width) if board[b][a] == "^"
    )


def findPath(board, pos, dir):
    state = (pos, dir)
    visited = []
    try:
        while True:
            visited.append(state)
            if len(visited) > len(board) * len(board) * 2:
                return True, visited
            pos, dir = state
            newX, newY = advance(pos, dir)
            if board[newY][newX] == "#":
                dir = turnRight(dir)
            else:
                pos = (newX, newY)
            state = (pos, dir)
    except IndexError:
        return False, visited


def run(board):
    initialPos = findStart(board)
    initialDir = (0, -1)
    _, visited = findPath(board, initialPos, initialDir)

    print(len(set(pos for pos, _ in visited)))

    cycles = []
    for pos in set(pos for pos, _ in visited):
        if pos == initialPos:
            continue
        newBoard = deepcopy(board)
        newBoard[pos[1]][pos[0]] = "#"
        cycle, _ = findPath(newBoard, initialPos, initialDir)
        cycles.append(cycle)

    print(len([c for c in cycles if c]))


# 2404 too high
# 1972 is right
