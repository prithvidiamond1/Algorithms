
# Depth First Search implementation for maze...

# from random import choice
from copy import deepcopy
import maze_builderV2 as mb

order = 10
space = ['X']+['_' for x in range(order)]+['X']
maze = [deepcopy(space) for x in range(order)]
maze.append(['X' for x in range(order+2)])
maze.insert(0, ['X' for x in range(order+2)])

# maze = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
#         ['X', 'S', 'X', '_', '_', '_', 'X', '_', '_', '_', 'X', 'X'],
#         ['X', '_', 'X', '_', 'X', '_', 'X', '_', 'X', '_', '_', 'X'],
#         ['X', '_', 'X', '_', 'X', '_', 'X', '_', 'X', 'X', '_', 'X'],
#         ['X', '_', 'X', '_', 'X', '_', 'X', '_', 'X', '_', '_', 'X'],
#         ['X', '_', 'X', '_', 'X', '_', 'X', '_', 'X', '_', 'X', 'X'],
#         ['X', '_', 'X', '_', 'X', '_', 'X', '_', 'X', '_', '_', 'X'],
#         ['X', '_', 'X', '_', 'X', '_', 'X', '_', 'X', 'X', '_', 'X'],
#         ['X', '_', 'X', '_', 'X', '_', 'X', '_', 'X', '_', '_', 'X'],
#         ['X', '_', 'X', '_', 'X', '_', 'X', '_', 'X', '_', 'X', 'X'],
#         ['X', '_', '_', '_', 'X', '_', '_', '_', 'X', '_', 'O', 'X'],
#         ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

finalpos = (order, order)

pos = (1, 1)

maze[pos[0]][pos[1]] = 'S'  # Initializing a start position
maze[finalpos[0]][finalpos[1]] = 'O'  # Initializing a end position

mb.mazebuilder(maze=maze)


def spit():
    for x in maze:
        print(x)

spit()
print()

mazemap = {}

def scan():  # Converts raw map/maze into a suitable datastructure.
    for x in range(1, order+1):
        for y in range(1, order+1):
            mazemap[(x, y)] = []
            t = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for z in t:
                if maze[z[0]][z[1]] == 'X':
                    pass
                else:
                    mazemap[(x, y)].append(z) 

scan()

# for x in mazemap:
#     print(x, ' ' ,mazemap[x])

path = [pos] # stack
impossible = False

while path[-1] != finalpos:
    curpos = path[-1]
    i = 0
    while i < len(mazemap[curpos]):
        if mazemap[curpos][i] in path:
            del mazemap[curpos][i]
        else:
            i += 1
    nextpos = None
    if mazemap[curpos] == []:
        while nextpos == None:
            try:
                wrongpos = path.pop(-1)
                if mazemap[wrongpos] == []:
                    pass
                else:
                    path.append(wrongpos)
                    # nextpos = choice(mazemap[wrongpos])
                    nextpos = mazemap[wrongpos][-1]
                    mazemap[wrongpos].remove(nextpos)
            except IndexError:
                impossible = True
                break
    else:
        # nextpos = choice(mazemap[curpos])
        nextpos = mazemap[curpos][-1]
    if impossible:
        break
    path.append(nextpos)

if not impossible:
    for x in path:
            if x == pos or x == finalpos:
                pass
            else:
                maze[x[0]][x[1]] = 'W'
else:
    print("This maze not solvable, Blyat!")
    print()

spit()
