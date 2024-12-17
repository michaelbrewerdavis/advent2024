import heapq


def parse(lines):
    return [list(line.strip()) for line in lines]


def findChar(board, c):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == c:
                return (x, y)
    return None


# (0, 1) => (1, 0) or (-1, 0)
# (-1, 0) => (0, 1) or (0, -1)
def findPath(board, start, end):
    pq = []
    considered = {}
    heapq.heappush(pq, (0, start, (1, 0)))

    def add(triplet):
        heapq.heappush(pq, triplet)

    while True:
        score, space, dir = heapq.heappop(pq)
        if (space, dir) in considered:
            continue
        considered[(space, dir)] = score

        if space == end:
            return score, considered
        else:
            if board[space[1] + dir[1]][space[0] + dir[0]] != "#":
                add((score + 1, (space[0] + dir[0], space[1] + dir[1]), dir))
            add((score + 1000, space, (dir[1], dir[0])))
            add((score + 1000, space, (-dir[1], -dir[0])))


def filterConsidered(board, start, end, considered, finalScore):
    candidates = [(end, (1, 0), finalScore), (end, (-1, 0), finalScore), (end, (0, 1), finalScore), (end, (0, -1), finalScore)]
    spaces = set([end])

    while len(candidates) > 0:
        space, dir, score = candidates.pop()
        if considered.get((space, dir)) == score:
            spaces.add(space)
            candidates.append(((space[0] - dir[0], space[1] - dir[1]), dir, score - 1))
            candidates.append((space, (dir[1], dir[0]), score - 1000))
            candidates.append((space, (-dir[1], -dir[0]), score - 1000))
    return spaces


def run(board):
    start = findChar(board, "S")
    end = findChar(board, "E")

    score, considered = findPath(board, start, end)
    print(score)
    onBestPath = filterConsidered(board, start, end, considered, score)
    print(len(onBestPath))
