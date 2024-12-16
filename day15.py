from copy import deepcopy

def parse(lines):
    a, b = "".join(lines).split("\n\n")
    m = list(map(lambda x: x.strip(), a.split("\n")))
    places = {}
    height = len(m)
    width = len(m[0])
    for y, row in enumerate(m):
        for x, c in enumerate(row):
            places[(x, y)] = c

    moves = "".join([l.strip() for l in b.split("\n")])
    return (height, width, places, moves)

def printMap(input):
    height, width, places = input
    for y in range(height):
        for x in range(width):
            print(places[(x,y)], end="")
        print()

def add(cell, dir):
    return (cell[0] + dir[0], cell[1] + dir[1])
    
def expandNeededSpace(places, space, dir):
    newNeeded = set()
    changed = False
    for s in space:
        if places[s] == '#':
            return False, None
        elif places[s] == '.':
            newNeeded.add(s)
        elif places[s] == 'O':
            changed = True
            newNeeded.add(add(s, dir))
        elif places[s] == '[' and dir[0] == 0:
            newNeeded.add(add(s, dir))
            newNeeded.add(add(add(s, (1, 0)), dir))
            changed = True
        elif places[s] == ']' and dir[0] == 0:
            newNeeded.add(add(s, dir))
            newNeeded.add(add(add(s, (-1, 0)), dir))
            changed = True
        elif places[s] == '[' or places[s] == ']':
            newNeeded.add(add(s, dir))
            changed = True

    return changed, newNeeded

def canMove(places, cell, dir):
    target = add(cell, dir)

    if places[target] == '#':
        return False
    elif places[target] == '.':
        return True
    elif places[target] == '[' and dir[0] == 0:
        return canMove(places, target, dir) and canMove(places, add(target, (1, 0)), dir)
    elif places[target] == ']' and dir[0] == 0:
        return canMove(places, target, dir) and canMove(places, add(target, (-1, 0)), dir)
    else:
        return canMove(places, target, dir)

def doMove(places, cell, dir):
    target = (cell[0] + dir[0], cell[1] + dir[1])
    if places[target] == '[' and dir[0] == 0:
        doMove(places, target, dir)
        doMove(places, add(target, (1, 0)), dir)
    elif places[target] == ']' and dir[0] == 0:
        doMove(places, target, dir)
        doMove(places, add(target, (-1, 0)), dir)
    elif places[target] != '.':
        doMove(places, target, dir)

    places[target] = places[cell]
    places[cell] = "."
    return target

def tryMove(places, cell, dir):
    target = (cell[0] + dir[0], cell[1] + dir[1])
    if canMove(places, cell, dir):
        doMove(places, cell, dir)
        return target
    else:
        return cell

def makeMove(mapx, robot, move):
    height, width, places = mapx
    dir = None
    if move == '>':
        dir = (1, 0)
    elif move == '<':
        dir = (-1, 0)
    elif move == 'v':
        dir = (0, 1)
    else:
        dir = (0, -1)

    return tryMove(places, robot, dir) or robot
    

def findRobot(mapx):
    height, width, places = mapx
    for x in range(width):
        for y in range(height):
            if places[(x, y)] == '@':
                return (x, y)
    raise NotImplementedError

def run1(input):
    mapx = deepcopy(input[0:3])
    robot = findRobot(mapx)
    moves = input[3]
    for move in moves:
        robot = makeMove(mapx, robot, move)

    total = 0
    for (x, y) in (places := mapx[2]):
        if places[(x,y)] == 'O':
            total += 100 * y + x 
    print(total)

def expandMap(input):
    oheight, owidth, oplaces, moves = input
    height = oheight
    width = 2 * owidth
    places = {}
    for x, y in oplaces:
        c = oplaces[(x, y)]
        if c == '#':
            c2 = '##'
        elif c == 'O':
            c2 = '[]'
        elif c == '@':
            c2 = '@.'
        else:
            c2 = '..'

        places[(2*x, y)] = c2[0]
        places[(2*x+1, y)] = c2[1]

    return height, width, places

def run2(input):
    mapx = expandMap(input)
    moves = input[3]
    robot = findRobot(mapx)
    for move in moves:
        robot = makeMove(mapx, robot, move)
    
    total = 0
    for (x, y) in (places := mapx[2]):
        if places[(x,y)] == '[':
            total += 100 * y + x 
    print(total)

def run(input):
    run1(input)
    run2(input)