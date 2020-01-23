
from copy import deepcopy
from math import inf
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

mb.mazebuilder(maze)

def spit():
    for x in maze:
        print(x)

# def move(curpos, movement): #curpos = tuple = (row, column)
#     if movement == 'u': #UP
#         return (curpos[0]-1, curpos[1])
#     elif movement == 'd':  # DOWN
#         return (curpos[0]+1, curpos[1])
#     elif movement == 'l':  # LEFT
#         return (curpos[0], curpos[1]-1)
#     elif movement == 'r':  # RIGHT
#         return (curpos[0], curpos[1]+1)

# Sample Movement
# maze[pos[0]][pos[1]] = '_'
# pos = move(pos, 'r')
# maze[pos[0]][pos[1]] = 'S'

spit()
print()

mazemap = {}

def scan(): # Converts raw map/maze into a suitable datastructure.
    for x in range(1, order+1):
        for y in range(1, order+1):
            mazemap[(x, y)] = {}
            t = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for z in t:
                # print(z[0], z[1], maze[z[0]][z[1]])
                if maze[z[0]][z[1]] == 'X':
                    pass
                else:
                    mazemap[(x, y)][z] = 1

scan()


# Dijkstra's algorithm
# # '_' - 1

unvisited = deepcopy(mazemap)
distances = {} # Stores shortest possible distance of each node
paths = {}  # Stores last node through which shortest path was acheived for each node

for node in unvisited: # Initialisation of distance information for each node
    if node == pos:
        distances[node] = 0 # Starting location...
    else:
        distances[node] = inf

while unvisited != {}:
    curnode = None 
    for node in unvisited:
        if curnode == None:
            curnode = node
        elif distances[node] < distances[curnode]:
            curnode = node
        else:
            pass

    for childnode, length in mazemap[curnode].items(): #cannot use unvisited map is it will keep changing in the loop
        if length + distances[curnode] < distances[childnode]:
            distances[childnode] = distances[curnode] + length
            paths[childnode] = curnode
    
    unvisited.pop(curnode)


# for x in distances:
#     print(x,':',distances[x])

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
    # print(finalpath)
    # print()

    for x in finalpath:
        if x == pos or x == finalpos:
            pass
        else:
            maze[x[0]][x[1]] = 'W'
else:
    print("This maze not solvable, Blyat!")
    print()

spit()
