import sys, re

g = {}
for line in sys.stdin:
    ID, *neighs = re.findall(r'\w+', line)
    g[int(ID)] = list(map(int,neighs))

groups, cnt_0, vis = 0, 0, set()
for root in range(max(g.keys()) + 1):
    if not root in vis:
        groups += 1
        vis.add(root)
        S = [root]
        while S:
            cnt_0 += root == 0
            for ne in g[S.pop()]:
                if not ne in vis:
                    S.append(ne)
                    vis.add(ne)
print('Part 1: {:d}'.format(cnt_0))
print('Part 2: {:d}'.format(groups))
