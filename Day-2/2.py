import sys

rows = list(filter(lambda l:l, map(lambda l: list(map(lambda x: int(x.strip()), l.split())), sys.stdin.readlines())))
char_functions = [
    ('Part 1', (lambda l: max(l) - min(l))),
    ('Part 2', (lambda l: sum((x//y) * (x/y == int(x/y)) for x in l for y in l) - len(l)))
    ]

for part, f in char_functions:
    print('{:s}: {:d}'.format(part, sum(map(f, rows))))
