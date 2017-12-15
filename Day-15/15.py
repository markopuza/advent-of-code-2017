def gen(start, factor, modbitval=0, M=2147483647, mask=(1<<16)-1):
    while 1:
        start = start * factor % M
        while start & modbitval:
            start = start * factor % M
        yield start & mask

for part, A, B, rep in [(1, gen(883,16807), gen(879,48271), int(4e7)), (2, gen(883,16807,3), gen(879,48271,7), int(5e6))]:
    print('Part {:d}: {:d}'.format(part, sum(next(A) == next(B) for _ in range(rep))))
