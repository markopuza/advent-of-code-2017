'''
Idea:
    Keep track of the vector in which we are moving, while populating
    the array by the spiral.
'''

n = 289326
sqrtn = int(n ** 0.5) + 1
nxt = {(1,0):(0,-1), (0,-1):(-1,0), (-1,0):(0,1), (0,1):(1,0)}

# switch stores the points in the spiral where the direction changes
cnt, switch = 1, set([1])
for i in range(1, sqrtn):
    switch |= set([cnt + i, cnt + 2*i])
    cnt += 2*i

# initialize for part 2
L = [[0 for _ in range(sqrtn)] for _ in range(sqrtn)]
L[sqrtn//2][sqrtn//2] = 1
part2_answer = 0

vx, vy = 1, 0 # vector of movement
x, y = sqrtn//2, sqrtn//2

for i in range(2, n + 1):
    x, y = x + vx, y + vy
    if i in switch:
        vx, vy = nxt[(vx,  vy)]
    if not part2_answer:
        L[x][y] = sum(L[x+ii][y+jj] for ii in [-1,0,1] for jj in [-1,0,1])
        if L[x][y] > n:
            part2_answer = L[x][y]

print('Part 1: {:d}'.format(abs(x - sqrtn//2) + abs(y - sqrtn//2)))
print('Part 2: {:d}'.format(part2_answer))
