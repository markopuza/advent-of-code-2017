import sys

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
grid = [list(line) for line in sys.stdin]
x, y, v, answer, cnt = 0, grid[0].index('|'), (1, 0), '', 1

while 1:
    x, y, cnt = x + v[0], y + v[1], cnt + 1
    if grid[x][y] == '+' or grid[x][y].isalpha():
        answer += grid[x][y] if grid[x][y].isalpha() else ''
        try:
            v, = filter(lambda nv: nv != (-v[0],-v[1]) and grid[x+nv[0]][y+nv[1]] != ' ', dirs)
        except:
            break

print('Part 1: {:s}\nPart 2: {:d}'.format(answer, cnt))
