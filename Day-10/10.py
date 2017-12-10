from functools import reduce
inp = input()

def knot(rep, lengths):
    l = list(range(256))
    curr, skip = 0, 0
    for _ in range(rep):
        for length in lengths:
            rev = (l+l)[curr:curr+length][::-1]
            for i in range(length):
                l[(curr+i) % 256] = rev[i]
            curr += length + skip
            curr %= 256
            skip += 1
    return l

p1 = knot(1, list(map(int,inp.split(','))))
print('Part 1: {:d}'.format(p1[0] * p1[1]))

p2 = knot(64, bytes(inp, 'ascii') + bytes([17, 31, 73, 47, 23]))
hashed = ''.join(hex(reduce(lambda x,y: x^y, p2[16*i:16*i+16]))[2:].zfill(2) for i in range(16))
print('Part 2: {:s}'.format(hashed))
