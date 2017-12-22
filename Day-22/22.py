import sys
from copy import copy
from collections import defaultdict

leftturn = lambda d: {(0, 1):(-1, 0), (0, -1):(1, 0), (1, 0):(0, 1), (-1, 0):(0, -1)}[d] # R L D U
rightturn = lambda d: {(0, 1):(1, 0), (0, -1):(-1, 0), (1, 0):(0, -1), (-1, 0):(0, 1)}[d]
reverse = lambda d: (-d[0], -d[1])

grid = [list(map(lambda x: x == '#', line.strip())) for line in sys.stdin]
gridmap = defaultdict(lambda: 'C')
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]:
            gridmap[(i, j)] = 'I'

parts = [(1, {'I':rightturn, 'C': leftturn}, {'I':'C', 'C':'I'}, 10000), \
    (2, {'I':rightturn, 'C':leftturn, 'F':reverse, 'W':(lambda d: d)}, {'I':'F', 'C':'W', 'W':'I', 'F':'C'}, 10000000)]

for part, actions, nextstate, bursts in parts:
    gridd = copy(gridmap)
    x, y, d, res = len(grid)//2, len(grid[0])//2, (-1, 0), 0

    for _ in range(bursts):
        d = actions[gridd[(x, y)]](d)
        gridd[(x, y)] = nextstate[gridd[(x, y)]]
        res += gridd[(x, y)] == 'I'
        x, y = x + d[0], y + d[1]
        
    print('Part {:d}: {:d}'.format(part, res))
