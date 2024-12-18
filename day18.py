import heapq

def parse(lines):
    return [tuple(map(int, line.strip().split(","))) for line in lines]

MAP_SIZE = 70
INST_COUNT = 1024

# MAP_SIZE = 6
# INST_COUNT = 12

def printBoard(board):
    for line in board:
        print("".join(line))

def fillBoard(input, instCount):
    board = [["." for _ in range(MAP_SIZE+1)] for _ in range(MAP_SIZE+1)]
    for i in range(instCount):
        x, y = input[i]
        board[y][x] = '#'
    return board

def findDistance(board):
    searchTree = []
    heapq.heapify(searchTree)
    searched = set()
    heapq.heappush(searchTree, (0, (0, 0)))
    while len(searchTree) > 0:
        distance, (x, y) = heapq.heappop(searchTree)
        if (x, y) == (MAP_SIZE, MAP_SIZE):
            return distance
        if x < 0 or x > MAP_SIZE or y < 0 or y > MAP_SIZE:
            continue
        if (x,y) in searched:
            continue
        searched.add((x,y))
        if board[y][x] == '#':
            continue
        heapq.heappush(searchTree, (distance+1, (x+1, y)))
        heapq.heappush(searchTree, (distance+1, (x-1, y)))
        heapq.heappush(searchTree, (distance+1, (x, y+1)))
        heapq.heappush(searchTree, (distance+1, (x, y-1)))
    return None

def findBadByte(input):
    def _findBadByte(input, min, max):
        if min == max:
            return min
        point = (min + max + 1) // 2
        board = fillBoard(input, point)
        distance = findDistance(board)
        if distance:
            return _findBadByte(input, point, max)
        else:
            return _findBadByte(input, min, point - 1)
    return _findBadByte(input, INST_COUNT, len(input) - 1)

def run(input):
    board = fillBoard(input, INST_COUNT)
    distance = findDistance(board)
    print(distance)

    badByte = findBadByte(input)
    print(badByte, input[badByte])