import math
import itertools


def parse(lines):
    return [list(line.strip()) for line in lines]


def printMap(map):
    for line in map:
        print("".join(line))


def mapNodes(map):
    nodes = {}
    for y, line in enumerate(map):
        for x, c in enumerate(line):
            if c != ".":
                existingNodes = nodes.get(c, [])
                existingNodes.append((x, y))
                nodes[c] = existingNodes
    return nodes


def validForMap(map, node):
    x, y = node
    return x >= 0 and x < len(map[0]) and y >= 0 and y < len(map)


def antinodes1(map, node1, node2):
    dx = node1[0] - node2[0]
    dy = node1[1] - node2[1]
    return [
        node
        for node in [(node1[0] + dx, node1[1] + dy), (node2[0] - dx, node2[1] - dy)]
        if validForMap(map, node)
    ]


def antinodes2(map, node1, node2):
    dx = node1[0] - node2[0]
    dy = node1[1] - node2[1]
    gcd = math.gcd(dx, dy)
    dx = int(dx / gcd)
    dy = int(dy / gcd)

    antinodes = set()
    for i in itertools.count():
        pt = (node1[0] + i * dx, node1[1] + i * dy)
        if validForMap(map, pt):
            antinodes.add(pt)
        else:
            break
    for i in itertools.count():
        pt = (node1[0] - i * dx, node1[1] - i * dy)
        if validForMap(map, pt):
            antinodes.add(pt)
        else:
            break
    return antinodes


def countAntinodes(map, nodes, method):
    allAntinodes = set()

    for key in nodes:
        for i, left in enumerate(nodes[key]):
            for right in nodes[key][i + 1 :]:
                an = method(map, left, right)
                for a in an:
                    allAntinodes.add(a)
                for x, y in an:
                    try:
                        map[y][x] = "#"
                    except IndexError:
                        pass

    return len(allAntinodes)


def run(map):
    nodes = mapNodes(map)

    print(countAntinodes(map, nodes, antinodes1))
    print(countAntinodes(map, nodes, antinodes2))
