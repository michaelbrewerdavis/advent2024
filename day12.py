from copy import deepcopy


def parse(lines):
    return [list(line.strip()) for line in lines]


def findRegion(map, value, cells, toSearch):
    while len(toSearch) > 0:
        nextX, nextY = toSearch.pop()
        if nextX < 0 or nextX >= len(map[0]) or nextY < 0 or nextY >= len(map):
            continue
        if map[nextY][nextX] == value:
            map[nextY][nextX] = None
            cells.append((nextX, nextY))
            toSearch += [
                (nextX + 1, nextY),
                (nextX - 1, nextY),
                (nextX, nextY + 1),
                (nextX, nextY - 1),
            ]
    return cells


def findRegions(map):
    map = deepcopy(map)
    regions = []
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] is None:
                continue
            region = findRegion(map, map[y][x], [], [(x, y)])
            regions.append(region)
    return regions


def calculatePerimeter(map, region, lookup):
    perimeter = []
    for cell in region:
        x, y = cell
        value = lookup[cell]
        neighbors = [(x + 1, y, ">"), (x - 1, y, "<"), (x, y + 1, "v"), (x, y - 1, "^")]
        for nx, ny, dir in neighbors:
            if (
                nx < 0
                or nx >= len(map[0])
                or ny < 0
                or ny >= len(map)
                or lookup[(nx, ny)] != value
            ):
                perimeter.append((nx, ny, dir))

    return perimeter


def consolidateSides(perimeter):
    lookup = {}
    sides = []
    for x, y, dir in perimeter:
        lookup[(x, y, dir)] = dir

    for key in lookup:
        if lookup[key] is None:
            continue
        side = []
        _, _, value = key
        possible = [key]
        while len(possible) > 0:
            checkKey = possible.pop()
            checkX, checkY, checkVal = checkKey
            if lookup.get(checkKey) == value:
                side.append(checkKey)
                lookup[checkKey] = None
                if value == "^" or value == "v":
                    possible += [
                        (checkX - 1, checkY, checkVal),
                        (checkX + 1, checkY, checkVal),
                    ]
                else:
                    possible += [
                        (checkX, checkY - 1, checkVal),
                        (checkX, checkY + 1, checkVal),
                    ]
        sides.append(side)
    return sides


def run(input):
    regions = findRegions(input)
    lookup = {}
    for i, region in enumerate(regions):
        for cell in region:
            lookup[cell] = i

    totalPrice = 0
    totalDiscountPrice = 0

    for i, region in enumerate(regions):
        area = len(region)
        perimeter = calculatePerimeter(input, region, lookup)
        price = area * len(perimeter)
        totalPrice += price

        sides = consolidateSides(perimeter)
        discountPrice = area * len(sides)
        totalDiscountPrice += discountPrice

    print(totalPrice)
    print(totalDiscountPrice)
