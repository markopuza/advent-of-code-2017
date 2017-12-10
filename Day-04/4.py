import sys
passphrases = list(map(lambda l: l.split(), sys.stdin.readlines()))

print('Part 1: {:d}'.format(sum(p and len(p) == len(set(p)) for p in passphrases)))
print('Part 2: {:d}'.format(sum(p and len(p) == len(set(map(lambda x: tuple(sorted(list(x))), p))) for p in passphrases)))
