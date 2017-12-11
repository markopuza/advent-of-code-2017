posmap = {'n':(-1,1), 's':(1,-1), 'nw':(-1,0), 'ne':(0,1), 'sw':(0,-1), 'se':(1,0)}
distance = lambda x, y: min(abs(x), abs(y)) + abs(abs(x) - abs(y)) if x*y < 0 else x + y

x, y, furthest, pos = 0, 0, 0, input().split(',')
for direction in pos:
    x += posmap[direction][0]
    y += posmap[direction][1]
    furthest = max(furthest, distance(x, y))

print('Part 1: {:d}'.format(distance(x, y)))
print('Part 2: {:d}'.format(furthest))
