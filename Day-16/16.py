import sys

def permute(moves, programs):
    programs = list(programs)
    for move in moves:
        if move[0] == 's':
            x = int(move[1:])
            programs = programs[-x:] + programs[:-x]
        elif move[0] == 'x':
            x, y = map(int, move[1:].split('/'))
            programs[x], programs[y] = programs[y], programs[x]
        else:
            x, y = move[1], move[3]
            px, py = programs.index(x), programs.index(y)
            programs[px], programs[py] = y, x
    return ''.join(programs)

alph, M = 'abcdefghijklmnop', sys.stdin.read().strip().split(',')
print('Part 1: {:s}'.format(''.join(permute(M, alph))))

cycle_length, curr, memo = 1, permute(M, alph), {0:alph}
while curr != alph:
    memo[cycle_length] = curr
    curr, cycle_length = permute(M, curr), cycle_length + 1

print('Part 2: {:s}'.format(memo[10 ** 9 % cycle_length]))
