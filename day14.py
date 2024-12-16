import blessed
import re
from functools import partial
import time

term = blessed.Terminal()

SIZEX=101
SIZEY=103
# SIZEX = 11
# SIZEY = 7

def parse(lines):
    matches = [re.match(r"p=(.*),(.*) v=(.*),(.*)", line).groups() for line in lines] 
    nums = [list(map(int, match)) for match in matches]
    # return nums
    return [((a, b), (c, d)) for a, b, c, d in nums]

def advance(steps, robot):
    pos, dir = robot
    posx, posy = pos
    dirx, diry = dir

    newPosx = (posx + steps * dirx) % SIZEX
    newPosy = (posy + steps * diry) % SIZEY

    return ((newPosx, newPosy), dir)

def quadrants(robots):
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for robot in robots:
        pos, _ = robot
        # print(robot)
        posx, posy = pos
        # 11 - 0-4, 5, 6-10
        if posx < SIZEX // 2:
            if posy < SIZEY // 2:
                q1 += 1
            elif posy > SIZEY // 2:
                q2 += 1
        elif posx > SIZEX // 2:
            if posy < SIZEY // 2:
                q3 += 1
            elif posy > SIZEY // 2:
                q4 += 1
    return (q1, q2, q3, q4)

def draw(robots):
    for robot in robots:
        (x, y), _ = robot
        
        print(term.move_xy(x, y) + term.bright_green + "XXX")

def run(input):
    # print([pos for (pos, _) in input])
    print(term.clear)

    advanced = input
    i = 0

    while True:
        print(term.clear)
        print(term.home + str(i))
        draw(advanced)
        advanced = [pos for pos in list(map(partial(advance, 1), advanced))]
        i += 1
        time.sleep(0.5)

    # q1, q2, q3, q4 = quadrants(advanced)
    # print(q1*q2*q3*q4)