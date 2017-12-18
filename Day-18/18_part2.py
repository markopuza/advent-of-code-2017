import sys

instructions = [(ins, args) for ins, *args in map(lambda x: x.split(), sys.stdin.readlines())]
registers = {}
for i in [0, 1]:
    registers[i] = dict((l, 0) for l in 'abcdefgijklmnopqrstuvwxyz')
    registers[i]['p'] = i

def get_value(program, x):
    return int(x) if x[-1].isdigit() else registers[program][x]

curr, sent, wait, last_rcv = [0, 0], [[], []], [False, False], [-1, -1]
result = 0

while 1:
    for ID in [0, 1]:
        if wait[ID]:
            if sent[1 - ID]:
                registers[ID][last_rcv[ID]] = sent[1 - ID][0]
                del sent[1 - ID][0]
                wait[ID] = False
        else:
            ins, args = instructions[curr[ID]]
            if ins == 'snd':
                sent[ID].append(get_value(ID, args[0]))
                result += ID == 1
            elif ins == 'set':
                registers[ID][args[0]] = get_value(ID, args[1])
            elif ins == 'add':
                registers[ID][args[0]] += get_value(ID, args[1])
            elif ins == 'mul':
                registers[ID][args[0]] *= get_value(ID, args[1])
            elif ins == 'mod':
                registers[ID][args[0]] %= get_value(ID, args[1])
            elif ins == 'rcv':
                last_rcv[ID] = args[0]
                if sent[1 - ID]:
                    registers[ID][last_rcv[ID]] = sent[1 - ID][0]
                    del sent[1 - ID][0]
                else:
                    wait[ID] = True

        if not wait[ID]:
            if ins == 'jgz':
                if get_value(ID, args[0]) > 0:
                    curr[ID] += get_value(ID, args[1])
                else:
                    curr[ID] += 1
            else:
                curr[ID] += 1

    if min(curr) < 0 or max(curr) >= len(instructions):
        break
    if wait[0] and wait[1]:
        break

print('Part 2: {:d}'.format(result))
