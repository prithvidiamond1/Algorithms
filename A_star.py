
from copy import deepcopy
from math import inf, sqrt
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
            mazemap[(x, y)] = {}
            t = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for z in t:
                if maze[z[0]][z[1]] == 'X':
                    pass
                else:
                    mazemap[(x, y)][z] = [sqrt((pos[0]-z[0])**2+(pos[1]-z[1])**2),
                                        sqrt((finalpos[0]-z[0])**2+(finalpos[1]-z[1])**2)] # Euclidean distance to destination (Heuristic)

scan()

# for x in mazemap:
#     print(x, ':', mazemap[x])

unvisited = deepcopy(mazemap)
distances = {}
paths = {}

# Initialization of distances:
for node in unvisited:
    if node == pos:
        distances[node] = [0, sqrt((finalpos[0]-node[0])**2+(finalpos[1]-node[1])**2)]
    else:
        distances[node] = [inf, inf]

# for x in distances:
#     print(x, ':', distances[x])

while unvisited != {}:
    curnode = None
    for node in unvisited:
        if curnode == None:
            curnode = node
        elif (distances[node][0]+distances[node][1]) < (distances[curnode][0]+distances[curnode][1]):
            curnode = node
        else:
            pass

    for childnode, lengths in mazemap[curnode].items():
        # Length to nearby childnode - G length, Euclidean (Heuristic) length from curnode to finalpos - H length
        # G length + H length < Euclidean length to reach that childnode directly + Euclidean length to finalpos from that childnode = Better path found, update known distance and paths
        if lengths[0] + lengths[1] < distances[childnode][0] + distances[childnode][1]:
            distances[childnode] = [lengths[0], lengths[1]]
            paths[childnode] = curnode
        
    unvisited.pop(curnode)

# for x in distances:
#     print(x, ':', distances[x])

# print()

# for x in paths:
#     print(x, ':', paths[x])

# print()


def shortestroute(paths, start, end):
    shortestpath = []
    try:
        def rec(start, end):
            if end == start:
                shortestpath.append(end)
                return shortestpath[::-1]
            else:
                shortestpath.append(end)
                return rec(start, paths[end])
        return rec(start, end)
    except KeyError:
        return False

finalpath = shortestroute(paths, pos, finalpos)

if finalpath:
    for x in finalpath:
        if x == pos or x == finalpos:
            pass
        else:
            maze[x[0]][x[1]] = 'W'
else:
    print("This maze not solvable, Blyat!")
    print()

spit()
