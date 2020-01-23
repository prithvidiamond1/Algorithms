
# Maze generator - v1: Generates mazes that look like a village road layout with houses scattered here and there.
# Very basic and primitive maze generator...

from copy import deepcopy
from random import randint

order = 10
space = ['X']+['_' for x in range(order)]+['X']
maze = [deepcopy(space) for x in range(order)]
maze.append(['X' for x in range(order+2)])
maze.insert(0, ['X' for x in range(order+2)])

maze[1][1] = 'S'  # Initializing a start position
maze[order][order] = 'O'  # Initializing a end position

finalpos = (order, order)

pos = (1, 1)

def spit():
    for x in maze:
        print(x)

# spit()

# Rules:
# Not more than 5x2 or 2x5 (HorizontalxVertical) blocks
# No block connected.
# Every freespace must be connected to atleast two other freespaces. $$

blocks = []
freespaces =  [(x, y) for x in range(1, order+1) for y in range(1, order+1)]

def mazebuilder(maze):
    def blockbuilder(kind):
        param1 = param2 = 0
        double = randint(0, 1)
        if kind == 0:
            param2 = randint(3, 5)
            if double:
                param1 = 2
            else:
                param1 = 1
        else:
            param1 = randint(3, 5)
            if double:
                param2 = 2
            else:
                param2 = 1
        for a in range(blockstarter[0], blockstarter[0]+param2):
            for b in range(blockstarter[1], blockstarter[1]+param1):
                if (a+1, b) in blocks or (a-1, b) in blocks or (a, b+1) in blocks or (a, b-1) in blocks or (a, b) in blocks or (a+1, b+1) in blocks or (a-1, b+1) in blocks or (a+1, b-1) in blocks or (a-1, b-1) in blocks:
                    pass
                else:
                    if a > order+1 or b > order+1:
                        pass
                    else:
                        if maze[a][b] == 'X':
                            blocks.append((a, b))
                        else:
                            spaces = [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]
                            for c in spaces:
                                if maze[c[0]][c[1]] == 'X':
                                    break
                                else:
                                    maze[a][b] = 'X'
                                    blocks.append((a, b))


    for x in range(1, order+1):
        for y in range(1, order+1):
            if (x, y) in freespaces:
                t = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
                i = 0
                while i < len(t):
                    if maze[t[i][0]][t[i][1]] == 'X' or (t[i][0], t[i][1]) == pos or (t[i][0], t[i][1]) == finalpos:
                        del t[i]
                    else:
                        i += 1
                if len(t) > 2:
                    blockstarter = t[randint(0, len(t)-1)]
                    kind = randint(0, 1) # 0 - vertical, 1 - horizontal 
                    blockbuilder(kind)
                else:
                    pass


if __name__ == "__main__":
    mazebuilder(maze=maze)

    spit()

 
