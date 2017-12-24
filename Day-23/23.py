import sys
from collections import defaultdict

registers = defaultdict(int)
instructions = [line.strip().split() for line in sys.stdin]
curr = 0

def get_value(val):
    try:
        return int(val)
    except:
        return registers[val]

res = 0
while 0 <= curr < len(instructions):
    jumped = False
    typ, x, y = instructions[curr]
    if typ == 'set':
        registers[x] = get_value(y)
    elif typ == 'sub':
        registers[x] -= get_value(y)
    elif typ == 'mul':
        res += 1
        registers[x] *= get_value(y)
    elif typ == 'jnz':
        if get_value(x) != 0:
            curr += get_value(y)
            jumped = True
    if not jumped:
        curr += 1

print('Part 1: {:d}'.format(res))

def is_prime(n):
      if n <= 1:
            return False
      if n <= 3:
            return True
      if n % 2 == 0 or n % 3 == 0:
            return False
      for i in range(6, round(n ** 0.5) + 2, 6):
            if n % (i - 1) == 0 or n % (i + 1) == 0:
                  return False
      return True

r = 0
for n in range(109300, 126301, 17):
    if not is_prime(n):
        r += 1
print('Part 2: {:d}'.format(r))
