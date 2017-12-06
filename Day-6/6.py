a = list(map(int, input().split()))
time, memory = 0, {}

while tuple(a) not in memory:
    memory[tuple(a)] = time
    # redistribute
    i = a.index(max(a))
    value = a[i]
    a[i] = 0
    for j in range(i+1, i+value+1):
        a[j%len(a)] += 1
    time += 1

print('Part 1: {:d}'.format(time))
print('Part 2: {:d}'.format(time - memory[tuple(a)]))
