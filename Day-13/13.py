import sys

layers = list(eval('{' + ','.join([line for line in sys.stdin]) + '}').items())

print('Part 1: {:d}'.format(sum(i*d if i%(2*d-2)==0 else 0 for i,d in layers)))
delay = 0
while any((i+delay)%(2*d-2) == 0 for i,d in layers):
    delay += 1
print('Part 2: {:d}'.format(delay))
