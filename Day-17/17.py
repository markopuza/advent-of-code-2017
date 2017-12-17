step = 329

arr, curr = [0], 0
for i in range(1, 2017 + 1):
    curr = (curr + step) % i + 1
    arr.insert(curr - 1, i)

print('Part 1: {:d}'.format(arr[(arr.index(2017) + 1) % len(arr)]))

first, curr = -1, 0
for i in range(1, int(5e7) + 1):
    curr = (curr + step) % i + 1
    if curr-1 == 0:
        first = i
        
print('Part 2: {:d}'.format(first))
