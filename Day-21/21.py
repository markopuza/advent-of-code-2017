import sys

transforms = lambda x, y, n: [(x,y), (x,n-1-y), (n-1-x,y), (n-1-x,n-1-y), \
            (y,x), (y,n-1-x), (n-1-y,x), (n-1-y,n-1-x)] # group D3

rules = {}
for line in sys.stdin:
    fr, to = line.split(' => ')
    fr, to = fr.strip().split('/'), to.strip().split('/')
    n = len(fr)
    fr_transforms = [[['-' for _ in range(n)] for _ in range(n)] for _ in range(8)]
    for x in range(n):
        for y in range(n):
            for ind, (xx, yy) in enumerate(transforms(x, y, n)):
                fr_transforms[ind][xx][yy] = fr[x][y]

    for frt in fr_transforms:
        rules[tuple(map(tuple, frt))] = tuple(map(tuple, to))

for part, iterations in [(1,5), (2,18)]:
    grid = [list('.#.'), list('..#'), list('###')]
    
    for _ in range(iterations):
        factor = 2 if len(grid) % 2 == 0 else 3
        newgrid = [['.' for _ in range(len(grid) + len(grid)//factor)] for _ in range(len(grid) + len(grid)//factor)]

        for sx in range(len(grid)//factor):
            for sy in range(len(grid)//factor):
                thispart = [[grid[i][j] for j in range(sy*factor, (sy+1)*factor)] for i in range(sx*factor, (sx+1)*factor)]
                sub = rules[tuple(map(tuple,thispart))]
                for i in range(factor+1):
                    for j in range(factor+1):
                        newgrid[sx*(factor+1) + i][sy*(factor+1) + j] = sub[i][j]
        grid = newgrid
    print('Part {:d}: {:d}'.format(part, sum(row.count('#') for row in grid)))
