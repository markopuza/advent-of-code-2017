import sys
from collections import defaultdict

regs, max_value = defaultdict(int), 0
for line in sys.stdin:
    exec('regs[\'{:s}\'] {:s} {:s} {:s} regs[\'{:s}\'] {:s} {:s} else 0'.format(*line.split())
        .replace('inc', '+=').replace('dec', '-='))
    max_value = max(max_value, regs[line.split()[0]])

print('Part 1: {:d}'.format(max(regs.values())))
print('Part 2: {:d}'.format(max_value))
