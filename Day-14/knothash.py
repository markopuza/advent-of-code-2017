from functools import reduce

def knot(str, rep=64):
    l = list(range(256))
    curr, skip = 0, 0
    for _ in range(rep):
        for b in bytes(str, 'ascii') + bytes([17, 31, 73, 47, 23]):
            rev = (l+l)[curr:curr+b][::-1]
            for i in range(b):
                l[(curr+i) % 256] = rev[i]
            curr += b + skip
            curr %= 256
            skip += 1
    return ''.join(hex(reduce(lambda x,y: x^y, l[16*i:16*i+16]))[2:].zfill(2) for i in range(16))
