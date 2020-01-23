
# Maze generator - v2: Generates mazes that look like city streets (more or less...)

from copy import deepcopy
from random import randint, choice

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
    
    # Randomize inside while loop - Fail
    # Randomize outside while loop - Pass

    # rch = choice(['d', 'u', 'r', 'l'])
    b = 0
    while b < len(blocks):
        block = blocks[b]
        t = {'d':(block[0]+2, block[1]), 'u':(block[0]-2, block[1]), 'r':(block[0], block[1]+2), 'l':(block[0], block[1]-2)}
        rch = choice(['d', 'u', 'r', 'l'])
        z = t[rch]
        # if z[0] > order+1 or z[1] > order+1 or z[0] < 1 or z[1] < 1:
        if z[0] > order-2 or z[1] > order-2 or z[0] < 2+2 or z[1] < 2+2: # Decreased chance of having non solvable maze being generated...
            pass
        else:
            if maze[z[0]][z[1]] == 'X':
                if randint(0, 1):
                    set = None
                    if rch == 'u':
                        set = (z[0]+1, z[1])
                    elif rch == 'd':
                        set = (z[0]-1, z[1])
                    elif rch == 'r':
                        set = (z[0], z[1]-1)
                    elif rch == 'l':
                        set = (z[0], z[1]+1)
                    else:
                        pass
                    if maze[set[0]][set[1]] == '_':
                        # Checks so that no walls that block the entire way are formed
                        # Makes sure maze is solvable
                        sets, count = [(set[0]+1, set[1]), (set[0]-1, set[1]), (set[0], set[1]+1), (set[0], set[1]-1)], 0
                        for blyat in sets:
                            while blyat[0] != 0 and blyat[1] != 0 and blyat[0] != order+1 and blyat[1] != order+1:
                                ch = [(blyat[0]+1, blyat[1]), (blyat[0]-1, blyat[1]), (blyat[0], blyat[1]+1), (blyat[0], blyat[1]-1)]
                                suka = []
                                for i in ch:
                                    if ch not in suka:
                                        if maze[i[0]][i[1]] == 'X':
                                            blyat = i
                                            break
                                        else:
                                            pass
                                        suka.append(ch)
                                    else:
                                        pass
                                else:
                                    blyat = None
                                if blyat == None:
                                    break
                                else:
                                    pass
                            else:
                                count += 1
                        if count < 1:
                            maze[set[0]][set[1]] = 'X'
                            blocks.append(set)
                        else:
                            pass
                        # check1 = [(set[0], y) for y in range(1, order+1) if maze[set[0]][y]=='X']
                        # check2 = [(x, set[1]) for x in range(1, order+1) if maze[x][set[1]]=='X']
                        # if len(check1) == 9 or len(check2) == 9:
                        #     pass
                        # else:
                        #     maze[set[0]][set[1]] = 'X'
                        #     blocks.append(set)    
                    else:
                        pass 
                else:
                    pass
        b += 1


if __name__ == "__main__":
    mazebuilder(maze=maze)

    spit()

    
