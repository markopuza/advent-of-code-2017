import sys

l = list(map(int, sys.stdin.readlines()))

def simulate(L, update_function):
    pointer, steps = 0, 0
    while 1:
        try:
            old_value = L[pointer]
            L[pointer] = update_function(L[pointer])
            pointer += old_value
            steps += 1
        except:
            break
    return steps

update_fns = [
    ('Part 1', (lambda x: x+1)),
    ('Part 2', (lambda x: x-1 if x >= 3 else x+1))
]

for part, f in update_fns:
    print('{:s}: {:d}'.format(part, simulate(list(l), f)))
