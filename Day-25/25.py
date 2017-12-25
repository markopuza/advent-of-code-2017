rules = { # state : current value : (to write, move left/right, next state)
'A': {False: (1,1,'B'), True: (0,-1,'C')},
'B': {False: (1,-1,'A'), True: (1,-1,'D')},
'C': {False: (1,1,'D'), True: (0,1,'C')},
'D': {False: (0,-1,'B'), True: (0,1,'E')},
'E': {False: (1,1,'C'), True: (1,-1,'F')},
'F': {False: (1,-1,'E'), True: (1,1,'A')}
}

pointer, state, ones, steps = 0, 'A', set(), 12172063

for step in range(steps):
    to_write, move, next_state = rules[state][pointer in ones]
    ones.add(pointer) if to_write else ones.discard(pointer)
    pointer, state = pointer + move, next_state

print('Part 1: {:d}'.format(len(ones)))
