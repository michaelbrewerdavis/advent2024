def parse(lines):
    return [list(map(int, line.strip())) for line in lines]

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def getReachablePeaks(board, reachablePeaks, x, y, i):
    if i == 9:
        return set([(x, y)])
    else:
        peaks = set()
        for dir in DIRS:
            try:
                newX = x + dir[0]
                newY = y + dir[1]
                if newY < 0 or newY >= len(board) or newX < 0 or newX >= len(board):
                    raise IndexError 
                if board[newY][newX] == i+1:
                    peaks = peaks.union(reachablePeaks[newY][newX])
            except IndexError:
                pass
    return peaks

def findReachablePeaks(board, reachablePeaks, i):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == i:
                reachablePeaks[y][x] = getReachablePeaks(board, reachablePeaks, x, y, i)

def scoreTrailheads(board):
    peaks = [[set() for y in line] for line in board]
    for i in range(9, -1, -1):
        findReachablePeaks(board, peaks, i)

    score = 0
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == 0:
                score += len(peaks[y][x])

    return score

def getReachablePaths(board, paths, x, y, i):
    if i == 9:
        return 1
    else:
        numPaths = 0
        for dir in DIRS:
            try:
                newX = x + dir[0]
                newY = y + dir[1]
                if newY < 0 or newY >= len(board) or newX < 0 or newX >= len(board):
                    raise IndexError 
                if board[newY][newX] == i+1:
                    numPaths += paths[newY][newX]
            except IndexError:
                pass
    return numPaths

def findPaths(board, paths, i):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == i:
                paths[y][x] = getReachablePaths(board, paths, x, y, i)

def rateTrailheads(board):
    paths = [[0 for y in line] for line in board]
    for i in range(9, -1, -1):
        findPaths(board, paths, i)

    rating = 0
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == 0:
                rating += paths[y][x]

    return rating

def run(board):
    score = scoreTrailheads(board)
    print(score)

    rating = rateTrailheads(board)
    print(rating)

    