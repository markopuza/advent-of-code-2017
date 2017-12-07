import sys, re
from collections import defaultdict, Counter

g, inv_g, weights = defaultdict(list), defaultdict(list), {}
for line in sys.stdin:
    name, weight, *children = re.findall(r'\w+', line)
    weights[name] = int(weight)
    for child in children:
        g[name].append(child)
        inv_g[child].append(name)

root, = set(g.keys()) - set(inv_g.keys())
print('Part 1: "{:s}"'.format(root))

def check(r=root):
    chw = [check(child) for child in g[r]]
    if len(set(chw)) > 1 and len(g[r]) > 2: # only works if the faulty node has > 2 siblings
        (should_have, _), (has, _) = Counter(chw).most_common()
        print('Part 2: node "{:s}" should weigh {:d}'.format(g[r][chw.index(has)], should_have - has + weights[g[r][chw.index(has)]]))
        sys.exit(0)
    return weights[r] + sum(chw)
check()
