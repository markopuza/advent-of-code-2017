s = list(map(int, list(input().strip())))
n = len(s)

for part, offset in enumerate([1, n//2]):
    print('Part {:d}: {:d}'.format(part+1, sum(s[i]*(s[i]==s[(i+offset)%n]) for i in range(n))))
