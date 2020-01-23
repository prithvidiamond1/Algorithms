
# Breadth First Search implementation for maze...

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

queue, visited = [pos], {pos:None}
impossible = None

while finalpos not in visited:
    nextqueue = []
    for x in queue:
        for y in mazemap[x]:
            if y in visited:
                pass
            else:
                nextqueue.append(y)
                visited[y] = x
    if nextqueue == []:
        impossible = True
        break
    else:
        del queue[:]
        queue.extend(nextqueue)

# for x in visited:
#     print(x, " ", visited[x])

def shortestroute(paths, start, end):
    shortestpath = []
    def rec(start, end):
        if end == start:
            shortestpath.append(end)
            return shortestpath[::-1]
        else:
            shortestpath.append(end)
            return rec(start, paths[end])
    return rec(start, end)

if impossible == None:
    finalpath = shortestroute(visited, pos, finalpos)
    for x in finalpath:
        if x == pos or x == finalpos:
            pass
        else:
            maze[x[0]][x[1]] = 'W'
else:
    print("This maze not solvable, Blyat!")
    print()

spit()
