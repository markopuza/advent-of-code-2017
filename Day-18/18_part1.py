import sys

instructions = [(ins, args) for ins, *args in map(lambda x: x.split(), sys.stdin.readlines())]
registers = dict((l, 0) for l in 'abcdefgijklmnopqrstuvwxyz')

def get_value(x):
    return int(x) if x[-1].isdigit() else registers[x]

last_played, curr = -1, 0
while 1:
    ins, args = instructions[curr]
    if ins == 'snd':
        last_played = get_value(args[0])
    elif ins == 'set':
        registers[args[0]] = get_value(args[1])
    elif ins == 'add':
        registers[args[0]] += get_value(args[1])
    elif ins == 'mul':
        registers[args[0]] *= get_value(args[1])
    elif ins == 'mod':
        registers[args[0]] %= get_value(args[1])
    elif ins == 'rcv':
        if get_value(args[0]):
            print('Part 1: {:d}'.format(last_played))
            break
    if ins == 'jgz':
        if get_value(args[0]) > 0:
            curr += get_value(args[1])
        else:
            curr += 1
    else:
        curr += 1
    if not 0 <= curr < len(instructions):
        break
