import sys

parts = [tuple(map(int, line.strip().split('/'))) for line in sys.stdin]
used = [False for _ in range(len(parts))]
max_strength, longest, longest_strength = 0, 0, 0

def dfs(curr, strength, length):
    global max_strength, longest, longest_strength
    max_strength = max(max_strength, strength)
    longest_strength = max(longest_strength, strength * (length == longest))
    if length > longest:
        longest, longest_strength = length, strength

    for i in range(len(parts)):
        if not used[i] and curr in parts[i]:
            used[i] = True
            dfs(parts[i][0] if parts[i][1] == curr else parts[i][1], strength + sum(parts[i]), length + 1)
            used[i] = False

dfs(0,0,0)
for part, ans in [(1, max_strength), (2, longest_strength)]:
    print('Part {:d}: {:d}'.format(part, ans))
